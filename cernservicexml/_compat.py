# -*- coding: utf-8 -*-
#
# This file is part of CERN Service XML
# Copyright (C) 2015 CERN.
#
# CERN Service XML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Python 2/3 compatibility module."""

from __future__ import absolute_import, print_function, unicode_literals

import sys

# Useful for very coarse version differentiation.
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:  # pragma: no cover
    string_types = str,
    text_type = str
    binary_type = bytes
else:    # pragma: no cover
    string_types = basestring,
    text_type = unicode
    binary_type = str
