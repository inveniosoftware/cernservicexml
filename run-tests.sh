#!/bin/sh
#
# This file is part of CERN Service XML
# Copyright (C) 2015 CERN.
#
# CERN Service XML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

pep257 cernservicexml && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test
