# -*- coding: utf-8 -*-
#
# This file is part of CERN Service XML
# Copyright (C) 2015 CERN.
#
# CERN Service XML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Publishing of service documents.

.. testsetup:: *

   from cernservicexml._compat import import_httpretty
   httpretty = import_httpretty()
   httpretty.enable()
   httpretty.register_uri(httpretty.POST, 'http://xsls.cern.ch',
                          body="", status=200)

.. testcleanup::

   httpretty.disable()


Usage:

>>> from cernservicexml import ServiceDocument, XSLSPublisher
>>> doc = ServiceDocument('myserviceid')
>>> XSLSPublisher.send(doc)
<Response [200]>
"""

from __future__ import absolute_import, print_function, unicode_literals

import requests

from ._compat import StringIO
from .document import ServiceDocument


class XSLSPublisher(object):

    """Publish a service document to an XSLS service."""

    @classmethod
    def send(cls, document, api_url='http://xsls.cern.ch'):
        """Send service document to XSLS."""
        assert isinstance(document, ServiceDocument)
        return requests.post(api_url, files=dict(
            file=StringIO(document.to_xml())))
