# -*- coding: utf-8 -*-
#
# This file is part of CERN Service XML
# Copyright (C) 2015 CERN.
#
# CERN Service XML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""CERN Service XML is a small library to generate a CERN XSLS Service XML."""

from __future__ import absolute_import, print_function, unicode_literals

from .document import ServiceDocument
from .publisher import XSLSPublisher
from .version import __version__

__all__ = ('ServiceDocument', 'XSLSPublisher', '__version__')
