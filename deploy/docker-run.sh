#!/usr/bin/env bash

set -u   # crash on missing env variables
set -e   # stop on any error
set -x

echo Collecting static files

# run uwsgi
exec uwsgi --emperor=.
