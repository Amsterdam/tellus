#!/usr/bin/env bash

set -u   # crash on missing env variables
set -e   # stop on any error
set -x   # print what we are doing

/deploy/docker-wait.sh

cd /app

./docker-code-check.sh
./docker-test.sh
