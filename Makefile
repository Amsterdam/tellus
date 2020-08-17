# This Makefile is based on the Makefile defined in the Python Best Practices repository:
# https://git.datapunt.amsterdam.nl/Datapunt/python-best-practices/blob/master/dependency_management/
#
# VERSION = 2020.01.29
.PHONY = help pip-tools install requirements update test init
dc = docker-compose
run = $(dc) run --rm
manage = $(run) dev python manage.py
pytest = $(run) test pytest $(ARGS)

build_version := $(shell git describe --tags --exact-match 2> /dev/null || git symbolic-ref -q --short HEAD)
build_revision := $(shell git rev-parse --short HEAD)
build_date := $(shell date --iso-8601=seconds)

init: clean build migrate           ## Init clean

help:                               ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

pip-tools:
	pip install pip-tools

install: pip-tools                  ## Install requirements and sync venv with expected state as defined in requirements.txt
	pip-sync requirements_dev.txt

requirements: pip-tools             ## Upgrade requirements (in requirements.in) to latest versions and compile requirements.txt
	pip-compile --upgrade --output-file requirements.txt requirements.in
	pip-compile --upgrade --output-file requirements_dev.txt requirements_dev.in

upgrade: requirements install       ## Run 'requirements' and 'install' targets

migrations:                         ## Make migrations
	$(manage) makemigrations $(ARGS)

migrate:                            ## Migrate
	$(manage) migrate

urls:
	$(manage) show_urls

build: export BUILD_DATE=$(build_date)
build: export BUILD_REVISION=$(build_revision)
build: export BUILD_VERSION=$(build_version)
build:                              ## Build docker image
	$(dc) build

push: build                         ## Push docker image to registry
	$(dc) push

push_semver:
	VERSION=$${VERSION} $(MAKE) push
	VERSION=$${VERSION%\.*} $(MAKE) push
	VERSION=$${VERSION%%\.*} $(MAKE) push

app:                                ## Run app
	$(run) --service-ports app

bash:                               ## Run the container and start bash
	$(run) dev bash

dev:                                ## Run the development app (and run extra migrations first)
	$(run) --service-ports dev

# lint:                               ## Execute lint checks
# 	$(run) test pytest /src $(ARGS)

# test: lint                          ## Execute tests
# 	$(run) test pytest /tests $(ARGS)

test:                               ## Execute tests
	$(run) test pytest /tests $(ARGS)

pdb:
	$(run) test pytest --pdb $(ARGS)

clean:                              ## Clean docker stuff
	$(dc) down -v --remove-orphans

env:                                ## Print current env
	env | sort
