# Python3 Data Science image based on Alpine

The image created by `Dockerfile.builder` is used
to build wheels for Alpine's *musl libc*,
for data science packages listed in ``requirements.txt``.
The different libc is the reason we cannot use existing
``manylinux1`` wheels, because they're built for glibc.

The ``build-wheels.sh`` script helps with a quirk of SciPy,
which won't build unless NumPy is installed first
(the ``numpy`` package is imported in its ``setup.py``).
It is called as the build container's entry point,
and download or creates all wheels referenced directly or
indirectly by ``requirements.txt``, writing them into the
``.pip-cache/repo`` directory that is mounted into the builder.
That means wheels already built are kept in the host's file system,
thus allowing very fast incremental builds after you added more requirements.

To start the wheel builder, use this command:

    docker build --build-arg "UID=$(id -u)" -t alpyne3ds-builder -f Dockerfile.builder . \
    && docker run --rm -it --mount type=bind,src=$PWD/.pip-cache,dst=/build/pip-cache alpyne3ds-builder

Build dependencies needed for compiling the extension packages
are installed in the ``apk`` call within ``Dockerfile.builder``.
You might need to adapt them when you add more dependencies
to ``requirements.txt``.
The same goes for runtime dependencies listed in ``Dockerfile.run``.

To manage the frozen versions in ``requirements.txt``, use these commands:

    test -e ~/.local/bin/pip-upgrade || pip install --user pip-upgrader
    ~/.local/bin/pip-upgrade --skip-package-installation requirements.txt
