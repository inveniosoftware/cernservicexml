# SPDX-FileCopyrightText: 2015, 2016 CERN.
# SPDX-License-Identifier: BSD-3-Clause

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
