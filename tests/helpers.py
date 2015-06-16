# -*- coding: utf-8 -*-
#
# This file is part of CERN Service XML
# Copyright (C) 2015 CERN.
#
# CERN Service XML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.


"""Test helpers."""

from __future__ import absolute_import, print_function, unicode_literals

import functools
import sys

PY34 = sys.version_info[0:2] >= (3, 4)


def import_httpretty():
    """Import HTTPretty and monkey patch Python 3.4 issue.

    See https://github.com/gabrielfalcao/HTTPretty/pull/193 and
    as well as https://github.com/gabrielfalcao/HTTPretty/issues/221.
    """
    if not PY34:
        import httpretty
    else:
        import socket
        old_SocketType = socket.SocketType

        import httpretty
        from httpretty import core

        def sockettype_patch(f):
            @functools.wraps(f)
            def inner(*args, **kwargs):
                f(*args, **kwargs)
                socket.SocketType = old_SocketType
                socket.__dict__['SocketType'] = old_SocketType
            return inner

        core.httpretty.disable = sockettype_patch(
            httpretty.httpretty.disable
        )

    return httpretty
