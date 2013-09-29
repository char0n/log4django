#!/bin/sh


. ./scripts/setup.sh

django-admin.py test -v 2 log4django $@

. ./scripts/teardown.sh
