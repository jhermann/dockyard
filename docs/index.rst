..  documentation master file

    Copyright ©  2018 Jürgen Hermann <jh@web.de>

    ## LICENSE_SHORT ##
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


=============================================================================
Welcome to the “dockyard” manual!
=============================================================================

.. image:: _static/img/logo.png

Basic Dockerfile templates and other Docker build helpers.


Contributing
------------

To create a working directory for this project, call these commands:

.. code-block:: shell

    git clone "https://github.com/jhermann/dockyard.git"
    cd "dockyard"
    . .env --yes
    invoke docs -b

Contributing to this project is easy, and reporting an issue or
adding to the documentation also improves things for every user.
You don’t need to be a developer to contribute.
See :doc:`CONTRIBUTING` for more.


Documentation Contents
----------------------

..  toctree::
    :maxdepth: 2
    :caption: Base Images

    usage


..  toctree::
    :maxdepth: 2
    :caption: How-Tos

    packaging-howto


..  toctree::
    :maxdepth: 2
    :caption: Miscellaneous

    CONTRIBUTING
    LICENSE


References
----------

Tools
^^^^^

-  `Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_
-  `PyInvoke <http://www.pyinvoke.org/>`_

Packages
^^^^^^^^

-  `Rituals <https://jhermann.github.io/rituals>`_


Indices and Tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
