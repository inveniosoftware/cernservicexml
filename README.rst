================
 CERNServiceXML
================

.. image:: https://travis-ci.org/inveniosoftware/cernservicexml.svg?branch=master
    :target: https://travis-ci.org/inveniosoftware/cernservicexml
.. image:: https://coveralls.io/repos/inveniosoftware/cernservicexml/badge.svg?branch=master
    :target: https://coveralls.io/r/inveniosoftware/cernservicexml
.. image:: https://pypip.in/v/cernservicexml/badge.svg
    :target: https://pypi.python.org/pypi/cernservicexml/
.. image:: https://pypip.in/d/cernservicexml/badge.svg
    :target: https://pypi.python.org/pypi/cernservicexml/

About
=====

CERNServiceXML is a small library to generate a CERN XSLS Service XML
and sending it to a remove service.

Installation
============

CERNServiceXML is on PyPI so all you need is: ::

    pip install cernservicexml

Documentation
=============

Documentation is readable at http://cernservicexml.readthedocs.io or can be
build using Sphinx: ::

    pip install Sphinx
    python setup.py build_sphinx

Testing
=======

Running the test suite is as simple as: ::

    python setup.py test

or, to also show code coverage: ::

    ./run-tests.sh
