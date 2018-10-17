# Python3 Data Science image based on Alpine

## Overview and Motivation

The Dockerfiles in this directory show how to build Alpine images
that have lots of dependencies to Python extension packages
(which need to be compiled for working with the *musl libc*).

See the [Base Images](https://kubedex.com/base-images/) blog post
for reasons why these days Alpine is not the only option anymore
for smallish images.
Especially so when the base size is relatively small to what the
application payload contributes to overall image size.

Still, this show-case has merit since it demonstrates how to use Docker for mass wheel building,
when ``manylinux1`` is not an option at all, or you want wheels
specifically compiled for a target platform.


## Wheel Builder

The image created by `Dockerfile.builder` is used
to build wheels for Alpine's *musl libc*,
for data science packages listed in ``requirements.txt``.
The different libc is the reason we cannot use existing
``manylinux1`` wheels, because they're built for glibc.

The ``build-wheels.sh`` script helps with a quirk of SciPy and other packages,
which won't build unless NumPy is installed first
(the ``numpy`` package is imported in their ``setup.py``).
It is called as the build container's entry point,
and downloads or creates all wheels referenced directly or
indirectly by ``requirements.txt``, writing them into the
``.pip-cache/repo`` directory that is mounted into the builder.
That means wheels already built are kept in the host's file system,
thus allowing very fast incremental builds after you added more requirements.

To start the wheel builder, use this command:

    docker build --build-arg "UID=$(id -u)" -t alpyne3ds-builder -f Dockerfile.builder . \
    && docker run --rm -it --mount type=bind,src=$PWD/.pip-cache,dst=/build/pip-cache alpyne3ds-builder

To use a local repository (PyPI mirror), add ``--env-file pip.env`` to the ``docker run`` call,
and create the ``pip.env`` file as follows:

    PIP_TRUSTED_HOST=devpi.local
    PIP_INDEX_URL=http://devpi.local:31415/root/pypi/+simple/

Build dependencies needed for compiling the extension packages
are installed in the ``apk`` call within ``Dockerfile.builder``.
You might need to adapt them when you add more dependencies
to ``requirements.txt``.
The same goes for runtime dependencies listed in ``Dockerfile.run``.

To manage the frozen versions in ``requirements.txt``, use these commands:

    test -e ~/.local/bin/pip-upgrade || pip install --user pip-upgrader
    ~/.local/bin/pip-upgrade --skip-package-installation requirements.txt


## Runtime Image

With all the wheels collected on disk, ``Dockerfile.run`` can install them
into the final runtime image.
This is also a multi-stage build (``alpyne3ds-installer`` ⇒ ``alpyne3ds``),
since we need to copy the wheels into the image for installation,
but we only want the expanded and installed packages in the runtime.

To build the ``alpyne3ds`` image, call Docker like this:

    docker build -t alpyne3ds -t alpyne3ds:$(git describe --tags) \
                 --target alpyne3ds -f Dockerfile.run .

    docker run --rm -it alpyne3ds  # opens a Python3 REPL

The resulting image has about 750 MB, compared to 4.7 GB of ``jupyter/scipy-notebook``.
Although right now, dependency lists still differ somewhat between those two,
that does not cause a factor 4 size difference.

To list the largest packages contributing to image size, try this:

    docker run --rm -it --entrypoint sh alpyne3ds -c \
           "du -sch /usr/lib/python3*/site-packages/* | egrep '[0-9]M' | sort -g"

For a practical example how to use the final image,
consider this command that starts a Jupyter notebook server:

    docker run --rm -it --expose 8888 -p 8888:8888 --entrypoint jupyter alpyne3ds \
           notebook --ip=0.0.0.0 --allow-root


If you add more packages, these commands are helpful for finding new auxiliary files to ``COPY`` over:

    docker build --target alpyne3ds-installer -t alpyne3ds-installer -f Dockerfile.run .
    docker run --rm -it --entrypoint sh alpyne3ds-installer -c \
        "find /usr -maxdepth 4 -type d -newer /root/build-stamp | grep -v dist-info | sort"
