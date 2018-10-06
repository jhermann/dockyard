# dockyard

> ![dockyard logo](https://raw.githubusercontent.com/jhermann/dockyard/master/docs/_static/img/logo.png) Basic Dockerfile templates and other Docker build helpers.

The contained files can be used either directly as base images,
or as templates to create new Dockerfiles with common
optimizations already baked in.
See the [main documentation](https://dockyard.readthedocs.io/)
on how to use the different parts of this project.


## Contributing

Contributing to this project is easy, and reporting an issue or
adding to the documentation also improves things for every user.
You don’t need to be a developer to contribute.
See [CONTRIBUTING](https://github.com/jhermann/dockyard/blob/master/CONTRIBUTING.md) for more.

As a documentation author or developer,
to **create a working directory** for this project,
call these commands:

```sh
git clone "https://github.com/jhermann/dockyard.git"
cd "dockyard"
command . .env --yes
invoke docs -b
```

For this to work, you might also need to follow some
[setup procedures](https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup)
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.

To **start a watchdog that auto-rebuilds documentation** and reloads the opened browser tab on any change,
call ``invoke docs -w -b`` (stop the watchdog using the ``-k`` option).
