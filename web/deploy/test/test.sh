#!/bin/sh

set -e
set -u
set -x

DIR="$(dirname $0)"

COMMIT_HASH=$(git rev-parse HEAD)

dc() {
	docker-compose -p ${COMMIT_HASH}_tellustest -f ${DIR}/docker-compose.yml $*
}

trap 'dc stop; dc rm --force; dc down' EXIT

dc stop
dc rm --force
dc down
dc pull
dc build

dc run --rm tests

dc stop
dc rm --force
dc down
