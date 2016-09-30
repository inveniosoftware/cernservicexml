# This file is part of CERNServiceXML
# Copyright (C) 2015, 2016 CERN.
#
# CERNServiceXML is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

# Use Python-2.7:
FROM python:2.7

# Install some prerequisites ahead of `setup.py` in order to profit
# from the docker build cache:
RUN pip install coveralls \
                httpretty \
                ipython \
                lxml \
                mock \
                pydocstyle \
                pytest \
                pytest-cache \
                pytest-cov \
                pytest-pep8 \
                requests \
                six \
                sphinx_rtd_theme

# Add sources to `code` and work there:
WORKDIR /code
ADD . /code

# Install cernservicexml:
RUN pip install -e .[docs]

# Run container as user `cernservicexml` with UID `1000`, which should match
# current host user in most situations:
RUN adduser --uid 1000 --disabled-password --gecos '' cernservicexml && \
    chown -R cernservicexml:cernservicexml /code

# Run test suite instead of starting the application:
USER cernservicexml
CMD ["python", "setup.py", "test"]
