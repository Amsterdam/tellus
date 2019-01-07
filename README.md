# Tellus
Tellus API and import  module.

## Development 

* Python 3.6 (required)
* Virtualenv (recommended)
* Docker-Compose (recommended)

    
### Local dockers
    # start the local docker containers
	docker-compose up -d --build
		
	# check out status using
	http://127.0.0.1:8107/status/health
	http://127.0.0.1:8107/status/data
	
### Local dockers and local server
    # start the local docker containers
	docker-compose up -d --build
	
	# create virtual environment (use the appropiate python binary)
	virtualenv -p /usr/local/bin/python3 venv
    source venv/bin/activate
    
    # install the requirements in the virtual env
    pip install -r requirements.txt
    
    # run database migrations
    export DJANGO_SETTINGS_MODULE=tellus.settings
    ./web/tellus_app/manage.py migrate
    
    # start server
    ./web/tellus_app/manage.py runserver  
   
   	# check out status using
    http://127.0.0.1:8000/status/health
    http://127.0.0.1:8000/status/data

### Importeer de meest recente database van acceptatie:
Als je SSH sleutel bekend is bij Datapunt kun je de acceptatie database
downloaden naar een lokaal draaiende versie van het Tellus project (in
het voorbeeld moet je `username` vervangen door jouw username bij Datapunt).

    docker-compose exec database update-db.sh tellus <username>

### Tellus import
#### Location of the datafiles
Login to Rattic and retrieve the tellus objectstore password for CloudVPS Tellus.

Login to https://stack.cloudvps.com/ with the user 'tellus'.

#### Run the import

    export DJANGO_SETTINGS_MODULE=tellus.settings
    export TELLUS_OBJECTSTORE_PASSWORD=XXX_from_step_above_XXX
    python ./web/tellus_app/importer.py
    
Check out the database tool pgadmin on host 'localhost' , port 5409.

 
