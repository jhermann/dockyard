..  documentation: docker-basics

    Copyright ©  2020 Jürgen Hermann <jh@web.de>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#############################################################################
Fundamental Docker
#############################################################################

Since there are plenty of documents on the web with details about basic Docker
use and writing state-of-the-art Dockerfiles, they're just listed here instead
of repeating the same information.


*******************
Reference Documents
*******************

* `Official Docker Documentation <https://docs.docker.com/>`_


*******************
Articles & How-Tos
*******************

* `Why Your Dockerized Application Isn’t Receiving Signals <https://hynek.me/articles/docker-signals/>`_ by Hynek Schlawack explains how to write your Dockerfile so that your main application actually receives shutdown signals sent by the Docker daemon. Otherwsise it cannot do an orderly cleanup, and instead is terminated forcibly after the shutdown timeout.

 See also `Gracefully Shutdown Docker Container <https://kkc.github.io/2018/06/06/gracefully-shutdown-docker-container/>`_.
