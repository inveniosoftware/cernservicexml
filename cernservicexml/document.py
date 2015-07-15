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

>>> from cernservicexml import ServiceDocument, Status
>>> doc = ServiceDocument('zenodo', status=Status.available)
>>> doc.add_numericvalue('users', 1000, desc="Number of users")
>>> xml = doc.to_xml()
"""

from __future__ import absolute_import, print_function, unicode_literals

import warnings
import xml.etree.ElementTree as ET
from datetime import datetime
from decimal import Decimal

from ._compat import binary_type, long_type, string_types, text_type


class Status(object):

    """Representation of availability status."""

    available = 'available'
    """Service is available for all users."""

    degraded = 'degraded'
    """Part of the service is not be working or some users are affected."""

    unavailable = 'unavailable'
    """Service is unavailable for all users."""


class ServiceDocument(object):

    """XSLS Service Document class.

    :param service_id: A unique service id.
    :param availability: An integer 0-100 indicating availability of
        service (*deprecated*, use ``status`` instead). Default: 100.
    :param status: Status of the service. Allowed values: ``available``,
        ``degraded`` or ``unavailable``. Default: ``available``.
    :param timestamp: Timestamp when the availability was calculated. Must
        be a datetime object. Default: now.
    :param availabilitydesc: Information about the availability.
    :param contact: Service contacts a string.
    :param webpage: Service website (any URI)
    :param availabilityinfo: Information about the service. Can contain
        HTML.

    .. versionchanged:: 0.2
       Added ``status`` parameter. Deprecated ``availability``
       parameter.
    """

    STATUSES = [Status.available, Status.degraded, Status.unavailable]
    """Allowed status values."""

    def __init__(self, service_id, status=None, timestamp=None,
                 availabilitydesc=None, contact=None, webpage=None,
                 availabilityinfo=None,
                 availability=None):
        """Initialize a service document."""
        if timestamp is not None:
            assert isinstance(timestamp, datetime)
        assert isinstance(service_id, string_types)

        if status is not None:
            assert status in self.STATUSES
            if availability is not None:
                raise AssertionError(
                    "Status and availability cannot be specified at the same "
                    "time. Please use only status."
                )
        elif availability is not None:
            warnings.warn(
                "Keyword argument 'availability' is deprecated and will be "
                "removed in v0.3. Please use keyword argument 'status' "
                "instead.", DeprecationWarning)
            assert isinstance(availability, int)
            assert availability >= 0 and availability <= 100
            self._availablity = availability
            if availability >= 0 and availability < 40:
                status = Status.unavailable
            elif availability >= 40 and availability < 70:
                status = Status.degraded
            elif availability >= 70 and availability <= 100:
                status = Status.available
        else:
            status = Status.available

        self.service_id = service_id
        self.status = status
        self.timestamp = timestamp or datetime.now()
        self.availabilitydesc = availabilitydesc
        self.contact = contact
        self.webpage = webpage
        self.availabilityinfo = availabilityinfo
        self.data = []

    @property
    def availability(self):
        """Get status as legacy availability percentage.

        .. deprecated:: 0.2
           Use of availability as percentage is deprecated. Please use
           ``status`` instead. Attribute will be removed in v0.3.
        """
        warnings.warn(
            "Use of availability attribute is deprecated. Please use status "
            "attribute instead.", DeprecationWarning)

        # If availability was set via constructor return that value.
        if hasattr(self, '_availablity'):
            return self._availablity

        # Otherwise, compute availability from status.
        if self.status == Status.available:
            return 100
        elif self.status == Status.degraded:
            return 50
        else:
            return 0

    def add_numericvalue(self, name, value, desc=None):
        """Add a numeric value metric.

        :param name: Numeric value id.
        :param value: An integer, float or Decimal object.
        :param desc: A description.

        """
        assert isinstance(name, string_types)
        assert isinstance(value, int) or isinstance(value, float) or \
            isinstance(value, Decimal) or isinstance(value, long_type)
        if desc is not None:
            assert isinstance(desc, string_types)
        self.data.append(dict(name=name, desc=desc, value=value))

    def to_xml(self):
        """Serialize service document to XML."""
        root = ET.Element('serviceupdate',
                          xmlns="http://sls.cern.ch/SLS/XML/update")
        ET.SubElement(root, 'id').text = self.service_id
        ET.SubElement(root, 'status').text = text_type(self.status)
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
