==================
 CERN Service XML
==================

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
CERN Service XML is a small library to generate a CERN XSLS Service XML and
sending it to a remove service.

Installation
============
CERN Service XML is on PyPI so all you need is: ::

    pip install cernservicexml

Documentation
=============
Documentation is readable at http://cernservicexml.readthedocs.org or can be
build using Sphinx: ::

    git submodule init
    git submodule update
    pip install Sphinx
    python setup.py build_sphinx

Testing
=======
Running the test suite is as simple as: ::

    python setup.py test

or, to also show code coverage: ::

    ./run-tests.sh
