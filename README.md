# docker-calves

> :whale: Basic Dockerfile templates and other Docker build helpers.

The contained files can be used either directly as base images,
or as templates to create new Dockerfiles with common
optimizations already baked in.


## Bionic + Python 3

This shows how to create a Python 3 image based on *Ubuntu Bionic*.
It is roughly 50 MiB larger than the Alpine-based equivalent,
but also comes with runtime essentials like
enabled locale, CA certificates, and ``glibc`` instead of the often problematic ``musl libc``.

The new ‘minimized’ Ubuntu images are a good base when you want to stay in known waters,
and your payload is not just a trivial script or something equally simple.
Alpine is a good choice for these small payloads, which also often just have
pure-Python dependencies, avoiding any trouble with the different libc.

To build both versions with clean caches and time each build, use this:

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

![biopy3-diff](https://raw.githubusercontent.com/jhermann/docker-calves/master/assets/biopy3-diff.png)

**TODO** Explain ‘optimization’ options / commands and their reason.
