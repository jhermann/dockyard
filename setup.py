# Shim for Sphinx and rituals
"""
Copyright (c) 2018  Jürgenm Hermann

The contained files can be used either directly as base images
or as templates to create new Dockerfiles with common optimizations already baked in.
"""

project = dict(
    name='dockyard',
    version='0.1.0',
    author='Jürgen Hermann',
    description='Basic Dockerfile templates and other Docker build helpers',
    long_description=__doc__,
)
