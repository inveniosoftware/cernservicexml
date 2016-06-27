# -*- coding: utf-8 -*-
#
# This file is part of CERNServiceXML
# Copyright (C) 2015, 2016 CERN.
#
# CERNServiceXML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Small library to generate a CERN XSLS Service XML."""

import os
import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

# Get the version string.  Cannot be done with import!
with open(os.path.join('cernservicexml', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

tests_require = [
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest-runner>=2.7.0',
    'pytest>=2.8.0',
    'coverage>=4.0',
    'httpretty>=0.8.0',
    'mock>=1.0',
    'lxml>=3.4',
    'pydocstyle>=1.0.0',
]

setup(
    name='cernservicexml',
    version=version,
    description=__doc__,
    author='Invenio Collaboration',
    author_email='info@invenio-software.org',
    url='https://github.com/inveniosoftware/cernservicexml',
    packages=['cernservicexml'],
    zip_safe=False,
    tests_require=tests_require,
    install_requires=[
        "requests>=1.1.0",
    ],
    extras_require={
        'docs': ['sphinx_rtd_theme'],
        'tests': tests_require,
    },
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ],
)
