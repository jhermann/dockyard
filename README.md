# dockyard

> :whale: Basic Dockerfile templates and other Docker build helpers.

The contained files can be used either directly as base images,
or as templates to create new Dockerfiles with common
optimizations already baked in.


## Bionic + Python 3

### Python 3.6 (Ubuntu default)

This shows how to create a Python 3 image based on *Ubuntu Bionic*.
It is roughly 50 MiB larger than the Alpine-based equivalent,
but also comes with runtime essentials like
enabled locale, CA certificates, and ``glibc`` instead of the often problematic ``musl libc``.

The new ‘minimized’ Ubuntu images are a good base when you want to stay in known waters,
and your payload is not just a trivial script or something equally simple.
Alpine is a good choice for these small payloads, which also often just have
pure-Python dependencies, avoiding any trouble with the different libc.

There is a simple and an optimized version of the Dockerfile,
with a few magic incantations added to the latter.
To build both versions with clean caches and timings for each build, use this:

```sh
docker system prune --all --force
( cd biopy3 \
    && docker pull ubuntu:bionic \
    && time docker build -f Dockerfile.simple -t biopy3-simple . \
    && time docker build -f Dockerfile.optimized -t biopy3 . \
)
```

Both images are built in about 15 seconds (on an Intel Core i7-6700 with SSD storage).
The ‘optimized’ one has a sub-second advantage regarding build time.
If you install more packages, the difference should get more pronounced.

The image sizes show a much clearer picture:
**129.6 MiB** for the ‘optimized’ version,
and **176.5 MiB** for the ‘simple’ one.

| Differences between simple and optimized Dockerfile versions |
| :---: |
| ![biopy3-diff](https://raw.githubusercontent.com/jhermann/docker-calves/master/assets/biopy3-diff.png) |

Here are the objectives for each of the changes as shown above:

* ``-o Acquire::Languages=none`` speeds up package list downloads by ignoring unneeded translation files.
* ``--no-install-recommends`` limits the installed package set to what you listed explicitly,
  and hard dependencies of that list – e.g. ``nodejs`` will otherwise install a *full* Python 2.7 for no good reason,
  instead of just ``python-minimal``. That improves both build times and image size.
* ``-o Dpkg::Options::=--force-unsafe-io`` switches off ``sync`` system calls during package expansion, speeding up package installation –
  since data is saved to a container layer shortly afterwards anyway, this is safe despite the option's name. ☺
* ``apt-get clean && rm -rf "/var/lib/apt/lists"/*`` removes any cached packages and metadata *before* the layer is stored.
  Both are things that we simply do not need in an immutable container.

And the ``env LANG=C`` before the ``apt-get`` commands suppresses
locale initialization warnings since locales are not generated yet.


### Python 3.7 (Deadsnakes PPA)

In ``biopy3/Dockerfile.deadsnakes`` the newest Python version is added,
as available from the Deadsnakes PPA.

Due to packging mechanics, this gets installed in addition to Ubuntu's default Python 3.6
– the resulting image size is 168.9 MiB (i.e. ~40 MiB more).
That means it is sensible to stick to 3.6 as long as you do not really use new language features
only available in version 3.7.
Another factor pointing in the same direction is that timely security updates are not guaranteed for the PPA release channel.

**TODO:** Look at other options like Conda, pyenv, or PyRun.
