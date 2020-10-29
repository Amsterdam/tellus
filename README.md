<img src="https://user-images.githubusercontent.com/205326/54359366-c6f20580-4662-11e9-80eb-2e17e56aec15.jpg" alt="tellus logo" width="200" align="right"/>

Tellus vehicle movements API and import module.

Exposes API to query vehicle movements counted by "Tellussen".
Tellussen are etched into the roads at several locations in Amsterdam and they count passing vehicles.
The API exposes vehicle counts, speed, direction and length at several locations in the city of Amsterdam.
These counts are available up to a resolution of an hour for authorized users.

## System overview

```                                                                      
                                                                               
            ┌────────────────────┐                                             
            │                    │                                             
            │                    │                                             
            │    Object store    │                                             
            │                    │                                             
            │                    │                                             
            └────────────────────┘                                             
                       │                                                       
                       │                                                       
                       │                                                       
       ┌ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ┐                                         
        Tellus repo    │                                                       
       │               ▼             │                                         
            ┌────────────────────┐                                             
       │    │                    │   │                                         
            │                    │                                             
       │    │      Importer      │───┼─────────────────────────────┐           
            │                    │                                 │           
       │    │                    │   │                             │           
            └────────────────────┘                                 ▼           
       │                             │                  ┌─────────────────────┐
                                                        │                     │
       │                             │                  │                     │
                                                        │      Database       │
       │                             │                  │                     │
                                                        │                     │
       │    ┌────────────────────┐   │                  └─────────────────────┘
            │                    │                                 │           
       │    │                    │   │                             │           
            │        API         │◀────────────────────────────────┤           
       │    │                    │   │                             │           
            │                    │                                 │           
       │    └────────────────────┘   │                             │           
                       │                                           │           
       └ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ┘                             │           
                       │                                           │           
                       │                                           │           
       ┌ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ┐                             │           
        Catalog repo   │                                           │           
       │               ▼             │                             ▼           
            ┌────────────────────┐                      ┌─────────────────────┐
       │    │                    │   │                  │                     │
            │                    │                      │                     │
       │    │  Tableau web data  │   │   Not used       │       Tableau       │
            │     connector      │─ ─ ─ (To slow) ─ ─ ─▶│                     │
       │    │                    │   │                  │                     │
            │                    │                      │                     │
       │    └────────────────────┘   │                  └─────────────────────┘
                                                                               
       └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘                                         
       
```

## Domain and class model

![Tellus class diagram](https://user-images.githubusercontent.com/205326/54351339-905ebf80-464f-11e9-89ef-5629fb2d236c.png)*Data model driving the API*

![Schematic voorburgwal tellus system](https://user-images.githubusercontent.com/205326/54361949-6239a980-4668-11e9-90f3-478eed9f5836.jpg)*Tellus system example with single "Tellus" box*

![Schematic wibautstraat tellus system](https://user-images.githubusercontent.com/205326/54361950-636ad680-4668-11e9-8f7c-b2375f2a5173.jpg)*Tellus system example with two "Tellus" boxes because the wires are physically separated by tram tracks*

## Development 

* Python 3.6 (required)
* Virtualenv (recommended)
* Docker-Compose (recommended)


The app can be developed using docker for everything or having only the database in docker.
After using either method the following end points will be available: 

* Basic web server and database health check: http://127.0.0.1:8107/status/health
* Basic database data health check: http://127.0.0.1:8107/status/data
* API overview: http://127.0.0.1:8107/tellus/
* A list view: http://127.0.0.1:8107/tellus/tellus/

### Local dockers

Start the database and webapp with:

```
docker-compose up -d --build
```
	
### Dockers DB with local server

Start the docker database
    
    docker-compose up -d --build database

Optionally use virtualenv:

    virtualenv -p /usr/local/bin/python3 venv
    source venv/bin/activate
    
Install the requirements:

    pip install -r requirements.txt
    pip install -r requirements-dev.txt

Run database migrations

    ./web/tellus_app/manage.py migrate

Start the server

    ./web/tellus_app/manage.py runserver


## Import

An import or copy of a running database is required to work with actual data.

### Perform import from raw data

The best way to get data into your environment is to run the import process on the raw data.
You will need access to the DataPunt object store.


Login to Rattic and retrieve the tellus objectstore password for CloudVPS Tellus.

Login to https://stack.cloudvps.com/ with the user 'tellus'.

Run the code

    export DJANGO_SETTINGS_MODULE=tellus.settings
    export TELLUS_OBJECTSTORE_PASSWORD=XXX_from_step_above_XXX
    python ./web/tellus_app/importer.py

 
### Copy acceptance database
If your SSH key is accepted by DataPunt you are able to copy the acceptance database
to you local project.

Use the following command:

    docker-compose exec database update-db.sh tellus <username>
 
Replace `<username>` with your DataPunt username.
And please note that the process may take very long.


# Project architectuur
Dit project volgt de standaard architectuur die we in meerdere projecten hanteren.

## Mappen structuur
- Alle code staat in `src/`, alle testcases in `tests/`. Scripts nodig tijdens deployments staan in `deploy/`.
- Er is een map `src/main/` met daarin Django settings en urls, uwsgi config en eventuele versie info.
- Overige configuratie files staan in de root (Makefile, Dockerfile, docker-compose bestanden, Jenkinsfile, Readme, requirements files en code-style configuraties).

## Makefile
De Makefile bevat enkele standaard targets:
- `pip-tools`, `install`, `requirements` en `upgrade` om dependencies te installeren en maintainen (zie volgende sectie)
- `migrations` en `migrate` om binnen docker migraties te maken en draaien
- `test` en `pdb` om testcases te draaien, eventueel met pdb om zo een interpreter te krijgen bij eventuele errors.
- `urls` om alle beschikbare (Django) urls te tonen
- `bash` om een bash shell van de app binnen docker te starten
- `build`, `push`, `clean` om de docker image te builden, naar de registry te pushen of alles op te schonen.
- `app` en `dev` om de applicatie lokaal te draaien.


## Docker gebruik
We maken gebruik van een multistage Dockerfile waarmee we drie versies van de image maken:
- `app` welke we op productie draaien
- `dev`, op basis van `app`, waar we tevens de dev requirements installeren. Hiermee kunnen we lokaal makkelijker debuggen
- `test` op basis van `dev` waarin we de testcases draaien.

Om te zorgen dat docker container lokaal toegang heeft tot bestanden in het host-system is het van belang het bestand `docker-compose.override.yml.example` te kopiëren naar `docker-compose.override.yml`, en daarin de `user` attributen aan te passen naar jouw eigen user id. Zodoende heeft de container de juiste rechten om bijvoorbeeld migraties aan te maken en weg te schrijven.

## Dependency management
Het project bevat twee bestanden die als bron voor de dependencies dienen:
- requirements.in
- requirements_dev.in

De eerste bevat requirements die nodig zijn om de applicatie in productie te draaien, de tweede bevat extra development requirements welke bijvoorbeeld nodig zijn om testcases uit te voeren.

Beide bestanden bevatten in de regel geen pinned dependencies (bijvoorbeeld Django==3.0.1), tenzij om duidelijke redenen een bepaalde versie specifiek nodig is in het project, en deze niet geüpgrade mag worden naar een latere versie.

Door middel van enkele Make targets maintainen we de requirements:
- `make install` installeert de bestaande requirements zoals gedefinieerd in requirements.txt en requirements_dev.txt.
- `make requirements` leest de `.in` bestanden in en maakt op basis daarvan de `requirements[_dev].txt` bestanden. Deze bevatten altijd de laatste versies van de dependencies, tenzij gepinned in de `requirements[_dev].in` bestanden.
- `make upgrade` voert `make requirements` uit, en installeert deze direct lokaal in de virtualenv.

Door deze werkwijze gelijkmatig in onze projecten door te voeren zijn we in staat in korte tijd vele projecten automatisch te upgraden. `make upgrade && make test` is voldoende om alle requirements te upgraden en te testen of alles naar behoren werkt.

## Deployments
Zoals in de Jenkinsfile gedefinieerd hanteren we de volgende deployment strategie:
- Alle pushes naar `master` deployen we naar acceptatie.
- Alle tags die aan het semver formaat voldoen (x.y.z*) deployen we naar productie.
Jenkins scant periodiek de repository en deployed automatisch.
