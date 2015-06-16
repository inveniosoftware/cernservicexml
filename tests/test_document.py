# -*- coding: utf-8 -*-
#
# This file is part of CERN Service XML
# Copyright (C) 2015 CERN.
#
# CERN Service XML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Service document tests."""

from __future__ import absolute_import, print_function, unicode_literals

from datetime import datetime
from decimal import Decimal

import pytest
from cernservicexml import ServiceDocument


def test_creation_simple():
    """Test creation of a service document."""
    doc = ServiceDocument('myserviceid')
    assert doc.service_id == 'myserviceid'
    assert isinstance(doc.timestamp, datetime)
    assert doc.availability == 100

    print(doc.to_xml())

    assert doc.to_xml() == \
        '<serviceupdate xmlns="http://sls.cern.ch/SLS/XML/update">' \
        '<id>myserviceid</id>' \
        '<availability>100</availability>' \
        '<timestamp>{0}</timestamp>' \
        '</serviceupdate>'.format(doc.timestamp.isoformat())

    dt = datetime(2015, 1, 1, 0, 0, 0)
    doc = ServiceDocument('anotherid', timestamp=dt,
                          availability=99)

    assert doc.to_xml() == \
        '<serviceupdate xmlns="http://sls.cern.ch/SLS/XML/update">' \
        '<id>anotherid</id>' \
        '<availability>99</availability>' \
        '<timestamp>2015-01-01T00:00:00</timestamp>' \
        '</serviceupdate>'


def test_creation_attrs():
    """Test non-mandatory attributes."""
    dt = datetime(2015, 1, 1, 0, 0, 0)
    doc = ServiceDocument(
        'myid',
        timestamp=dt,
        availabilitydesc='My description',
        contact='info@example.org',
        webpage='http://example.org',
        availabilityinfo='Extra info',
    )

    assert doc.to_xml() == \
        '<serviceupdate xmlns="http://sls.cern.ch/SLS/XML/update">' \
        '<id>myid</id>' \
        '<availability>100</availability>' \
        '<timestamp>2015-01-01T00:00:00</timestamp>' \
        '<availabilitydesc>My description</availabilitydesc>' \
        '<contact>info@example.org</contact>' \
        '<webpage>http://example.org</webpage>' \
        '<availabilityinfo>Extra info</availabilityinfo>' \
        '</serviceupdate>'


def test_outofbounds():
    """Test out of bounds values."""
    with pytest.raises(AssertionError):
        ServiceDocument(None)
    with pytest.raises(AssertionError):
        ServiceDocument(1234)
    with pytest.raises(AssertionError):
        ServiceDocument('id', timestamp='1234')
    with pytest.raises(AssertionError):
        ServiceDocument('id', availability=-1)
    with pytest.raises(AssertionError):
        ServiceDocument('id', availability=101)
    with pytest.raises(AssertionError):
        ServiceDocument('id', availability='100')
    doc = ServiceDocument('id')
    with pytest.raises(AssertionError):
        doc.add_numericvalue(1234, 'val')
    with pytest.raises(AssertionError):
        doc.add_numericvalue('name', 1234, desc=1234)
    with pytest.raises(AssertionError):
        doc.add_numericvalue('name', 'astring', desc=1234)


def test_numericvalue():
    """Test adding numeric data to service."""
    dt = datetime(2015, 1, 1, 0, 0, 0)
    doc = ServiceDocument('myid', timestamp=dt)
    doc.add_numericvalue('val1', 1234)
    doc.add_numericvalue('val2', 12.34)
    doc.add_numericvalue('val3', Decimal("0.1"))
    doc.add_numericvalue('val4', Decimal("0.1") + Decimal("0.2"))
    doc.add_numericvalue('val5', 1234, desc="a desc")

    assert doc.to_xml() == \
        '<serviceupdate xmlns="http://sls.cern.ch/SLS/XML/update">' \
        '<id>myid</id>' \
        '<availability>100</availability>' \
        '<timestamp>2015-01-01T00:00:00</timestamp>' \
        '<data>' \
        '<numericvalue name="val1">1234</numericvalue>' \
        '<numericvalue name="val2">12.34</numericvalue>' \
        '<numericvalue name="val3">0.1</numericvalue>' \
        '<numericvalue name="val4">0.3</numericvalue>' \
        '<numericvalue desc="a desc" name="val5">1234</numericvalue>' \
        '</data>' \
        '</serviceupdate>'
