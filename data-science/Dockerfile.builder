# Python 3 Data Science wheel builder for minimal Alpine image
#
# Docs:
#   http://gliderlabs.viewdocs.io/docker-alpine/
#
# Commands:
#   docker build --build-arg "UID=$(id -u)" -t alpyne3ds-builder -f Dockerfile.builder . && docker run --rm -it --mount type=bind,src=$PWD/.pip-cache,dst=/build/pip-cache alpyne3ds-builder
#

ARG UID=1000

# ~~~ Python3 Alpine Base ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM alpine AS alpyne3
ENV LANG=en_US.UTF-8
# Install Python3 and immediately do in-place tooling updates, in the same layer
RUN apk --update --no-cache add ca-certificates python3 \
    && python3 -m pip install --no-cache-dir -U pip setuptools wheel
ENTRYPOINT ["python3"]


# ~~~ Builder for Data Science Stack Wheels ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM alpyne3 AS alpyne3ds-builder
ARG UID
WORKDIR /build
RUN apk --update --no-cache add \
        build-base \
        freetype-dev \
        jpeg-dev \
        libpng-dev \
        llvm-dev \
        openblas-dev \
        python3-dev \
        sudo \
        ;
        # TESTING libhdf5-dev \
# lapack-dev seems to be part of openblas-dev

RUN adduser -h $PWD -G users -H -D -u ${UID} maintainer \
    && ( umask 0077 && echo "maintainer ALL=(ALL) NOPASSWD:ALL" >/etc/sudoers.d/maintainer ) \
    && chown -R ${UID} .

# Build wheels using the mounted cachedir
USER ${UID}
COPY --chown=maintainer:users requirements.txt build-wheels.sh ./
ENTRYPOINT ["/bin/sh", "/build/build-wheels.sh"]
