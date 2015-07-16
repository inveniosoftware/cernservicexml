===================================
 CERN Service XML v0.2.0 is released
===================================

CERN Service XML v0.2.0 was released on 2015-07-16

About
-----

CERN Service XML is a small library to generate a CERN XSLS Service XML.

What's new
----------

- Adds support for service status parameter in ``ServiceDocument``.
- Deprecates use of service availability percentage in ``ServiceDocument``.
  Please use service status parameter instead.
- Changes documentation theme to the standard non-Flask RTD one.
- Initial release of Docker configuration suitable for local developments.
  `docker-compose build` rebuilds the image, `docker-compose run --rm web
  python setup.py test` runs the test suite.

Installation
------------

   $ pip install cernservicexml

Documentation
-------------

   http://cernservicexml.readthedocs.org/en/v0.2.0

Homepage
--------

   https://github.com/inveniosoftware/cernservicexml

Good luck and thanks for choosing CERN Service XML.

| Invenio Development Team
|   Email: info@invenio-software.org
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: http://github.com/inveniosoftware
|   URL: http://invenio-software.org
