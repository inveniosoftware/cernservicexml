# -*- coding: utf-8 -*-
#
# This file is part of CERN Service XML
# Copyright (C) 2015 CERN.
#
# CERN Service XML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Publisher tests."""

from __future__ import absolute_import, print_function, unicode_literals

from datetime import datetime

import cgi
from cernservicexml import ServiceDocument, XSLSPublisher
from cernservicexml._compat import import_httpretty

httpretty = import_httpretty()

EXAMPLE_URL = "http://xsls.example.org"


@httpretty.activate
def test_xslspublisher_send():
    """."""
    httpretty.register_uri(httpretty.POST, EXAMPLE_URL, body="", status=200)

    dt = datetime(2015, 1, 1, 0, 0, 0)
    doc = ServiceDocument('myid', timestamp=dt)
    resp = XSLSPublisher.send(doc, api_url=EXAMPLE_URL)
    assert resp.status_code == 200

    # Parse multipart/form-data (not supported by HTTPretty)
    content_type = httpretty.last_request().headers['Content-Type'].split(';')
    content_type = [x.strip() for x in content_type]
    key, boundary = content_type[1].split("=")
    data = cgi.parse_multipart(httpretty.last_request().rfile,
                               {'boundary': boundary.encode('utf-8')})

    assert 'file' in data
    assert data['file'][0].decode('utf-8') == \
        '<serviceupdate xmlns="http://sls.cern.ch/SLS/XML/update">' \
        '<id>myid</id><availability>100</availability>' \
        '<timestamp>2015-01-01T00:00:00</timestamp></serviceupdate>'
