# -*- coding: utf-8 -*-
#
# This file is part of CERN Service XML
# Copyright (C) 2015 CERN.
#
# CERN Service XML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Creation of XSLS service documents.

Usage:

>>> from cernservicexml import ServiceDocument
>>> doc = ServiceDocument('zenodo')
>>> doc.add_numericvalue('users', 1000, desc="Number of users")
>>> xml = doc.to_xml()
"""

from __future__ import absolute_import, print_function, unicode_literals

import xml.etree.ElementTree as ET
from datetime import datetime
from decimal import Decimal

from ._compat import string_types, text_type, binary_type


class ServiceDocument(object):

    """XSLS Service Document class.

    :param service_id: A unique service id.
    :param availability: An integer 0-100 indicating availability of service.
        Default: 100.
    :param timestamp: Timestamp when the availability was calculated. Must be
        a datetime object. Default: now.
    :param availabilitydesc: Information about the availability.
    :param contact: Service contacts a string.
    :param webpage: Service website (any URI)
    :param availabilityinfo: Information about the service. Can contain HTML.
    """

    def __init__(self, service_id, availability=100, timestamp=None,
                 availabilitydesc=None, contact=None, webpage=None,
                 availabilityinfo=None):
        """Initialize a service document."""
        if timestamp is not None:
            assert isinstance(timestamp, datetime)
        assert isinstance(service_id, string_types)
        assert isinstance(availability, int)
        assert availability >= 0 and availability <= 100

        self.service_id = service_id
        self.availability = availability
        self.timestamp = timestamp or datetime.now()
        self.availabilitydesc = availabilitydesc
        self.contact = contact
        self.webpage = webpage
        self.availabilityinfo = availabilityinfo
        self.data = []

    def add_numericvalue(self, name, value, desc=None):
        """Add a numeric value metric.

        :param name: Numeric value id.
        :param value: An integer, float or Decimal object.
        :param desc: A description.

        """
        assert isinstance(name, string_types)
        assert isinstance(value, int) or isinstance(value, float) or \
            isinstance(value, Decimal)
        if desc is not None:
            assert isinstance(desc, string_types)
        self.data.append(dict(name=name, desc=desc, value=value))

    def to_xml(self):
        """Serialize service document to XML."""
        root = ET.Element('serviceupdate',
                          xmlns="http://sls.cern.ch/SLS/XML/update")
        ET.SubElement(root, 'id').text = self.service_id
        ET.SubElement(root, 'availability').text = text_type(self.availability)
        ET.SubElement(root, 'timestamp').text = self.timestamp.isoformat()

        for e in ['availabilitydesc', 'contact', 'webpage',
                  'availabilityinfo']:
            val = getattr(self, e)
            if val is not None:
                ET.SubElement(root, e).text = text_type(val)

        if self.data:
            data = ET.SubElement(root, 'data')

            for d in self.data:
                attrs = dict(name=d['name'])
                if d['desc']:
                    attrs['desc'] = d['desc']
                ET.SubElement(data, 'numericvalue', attrib=attrs).text = \
                    text_type(d['value'])

        res = ET.tostring(root)
        if isinstance(res, binary_type):
            res = res.decode('utf-8')

        return res
