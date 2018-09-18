#!/usr/bin/env bash

set -u   # crash on missing env variables
set -e   # stop on any error
set -x

echo make migrations...
python manage.py migrate

echo export DJANGO_SETTINGS_MODULE
export DJANGO_SETTINGS_MODULE=tellus.settings

echo export TELLUS_OBJECTSTORE_PASSWORD=XXXXXX
python importer.py

