#!/bin/sh

set -e
set -u

DIR="$(dirname $0)"

dc() {
	docker-compose -p tellus -f ${DIR}/docker-compose.yml $*
}

trap 'dc kill ; dc rm -f' EXIT

rm -rf ${DIR}/backups

dc build
dc pull
dc run --rm importer

mkdir -p ${DIR}/backups
dc exec -T database backup-db.sh tellus
dc down -v