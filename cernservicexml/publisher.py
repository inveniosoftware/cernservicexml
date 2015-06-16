# -*- coding: utf-8 -*-
#
# This file is part of CERN Service XML
# Copyright (C) 2015 CERN.
#
# CERN Service XML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Publishing of service documents.

Usage:

.. code-block:: python

    >>> from cernservicexml import ServiceDocument, XSLSPublisher
    >>> doc = ServiceDocument('myserviceid')
    >>> XSLSPublisher.send(doc)
"""

from __future__ import absolute_import, print_function, unicode_literals

import requests

from .document import ServiceDocument


class XSLSPublisher(object):

    """Publish a service document to an XSLS service."""

    @classmethod
    def send(cls, document, api_url='http://xsls.cern.ch'):
        """Send service document to XSLS."""
        assert isinstance(document, ServiceDocument)
        return requests.post(api_url, data=document.to_xml())
