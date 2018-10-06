# Shim for Sphinx and rituals
# -*- coding: utf-8 -*-
"""
Copyright (c) 2018  Juergenm Hermann

The contained files can be used either directly as base images
or as templates to create new Dockerfiles with common optimizations already baked in.
"""

project = dict(
    name='dockyard',
    version='0.1.0',
    author='Juergen Hermann',
    url='https://github.com/jhermann/dockyard',
    description='Basic Dockerfile templates and other Docker build helpers',
    long_description=__doc__,
)

if __name__ == '__main__':
    import sys

    for opt in sys.argv[1:]:
        if opt.startswith('--') and opt[2:] in project:
            print(project[opt[2:]])
