# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation
""" Project automation for Invoke.
"""
# Copyright ©  2018 Jürgen Hermann <jh@web.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import absolute_import, unicode_literals

import os
import shutil
import tempfile

from rituals.easy import *  # pylint: disable=redefined-builtin


@task(name='fresh-cookies',
    help={
        'mold': "git URL or directory to use for the refresh",
    },
)
def fresh_cookies(ctx, mold=''):
    """Refresh the project from the original cookiecutter template."""
    mold = mold or "https://github.com/Springerle/py-generic-project.git"  # TODO: URL from config
    tmpdir = os.path.join(tempfile.gettempdir(), "cc-upgrade-dockyard")

    if os.path.isdir('.git'):
        # TODO: Ensure there are no local unstashed changes
        pass

    # Make a copy of the new mold version
    if os.path.isdir(tmpdir):
        shutil.rmtree(tmpdir)
    if os.path.exists(mold):
        shutil.copytree(mold, tmpdir, ignore=shutil.ignore_patterns(
            ".git", ".svn", "*~",
        ))
    else:
        ctx.run("git clone {} {}".format(mold, tmpdir))

    # Copy recorded "cookiecutter.json" into mold
    shutil.copy2("project.d/cookiecutter.json", tmpdir)

    with pushd('..'):
        ctx.run("cookiecutter --no-input {}".format(tmpdir))
    if os.path.exists('.git'):
        ctx.run("git status")

namespace.add_task(fresh_cookies)


@task
def ci(ctx):
    """Perform continuous integration tasks."""
    opts = ['']

    # 'tox' makes no sense in Travis
    if os.environ.get('TRAVIS', '').lower() == 'true':
        opts += ['test.pytest']
    else:
        opts += ['test.tox']

    ctx.run("invoke --echo --pty clean --all build --docs check --reports{}".format(' '.join(opts)))

namespace.add_task(ci)
