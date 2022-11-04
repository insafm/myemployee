![screenshot](https://github.com/insafm/myemployee/blob/main/SCREENSHOT.png?raw=true)

WARNING: The env folder and its contents are all of contains confidential information. env files are used to load environment variables from an env file into the running process.

### MyEmployee Project Requirements
----

1. Login using your Gmail id.
2. Logged-in user can view a form to add employee details. There should be a name, employee code and other common fields.
3. On submitting the employee details, the page should redirect to the "Add Salary" page. This page should display employee name and employee number, sent from add employee page, in non editable text fields. The employee code should not be passed URL parameter.
4. Option for view, edit & delete employees

### Django Environment Variables
----

- ``` APPLICATION_NAME```: The name of the application.
- ``` DEBUG```: Debug mode. If on, will display details of error pages. If your app raises an exception when DEBUG is on, will display a detailed traceback, including a lot of metadata about the environment, such as all the currently defined Django settings (from base.py). Never deploy a site into production with DEBUG turned on.
- ``` DJANGO_SETTINGS_MODULE```: The Django settings module to use.
- ``` SECRET_KEY```: The secret key to use for cryptographic operations should be set to a unique, unpredictable value. Never deploy a site into production with the default secret key.
- ``` DATABASE_URL```: The URL of the database to use. You can choose from a variety of database engines.
- ``` ALLOWED_HOSTS```: The comma seperated hostnames that Django will use to access the site.
- ``` TIME_ZONE```: The timezone to use for the site.
- ``` ENABLE_LOGGING```: If on, will enable exception logging in rotated file handler.
- ``` ENABLE_AUTO_LOGGING```: If on, will enable auto exception logging in rotated file handler.
- ``` LOGGING_DIR```: The directory to use for exception logging.
- ``` ENABLE_DEBUG_TOOLBAR```: If on, will enable debug toolbar.

### Terminology
----

- Docker: A containerization technology that provides a simple, reliable, and secure way to run software.
- Dockerfile: A set of commands to build an image to be run as a container.
- Docker-Compose: A file defining how to run a multi-container Docker application.
- Docker-Machine: A tool for managing Docker containers.
- Docker-Registry: A Docker registry that stores images and allows you to share them with others.

### Run Docker Compose To Run The Application
----

- ``` docker-compose -f docker-compose.yml up ``` - Run the project environment.
- ``` docker-compose -f docker-compose.yml up --build -d ``` - Build the project environment and run it.
- ``` docker-compose -f docker-compose.yml -f docker-compose.production.yml up``` - Run the production environment.
- ``` docker-compose -f docker-compose.yml -f docker-compose.production.yml up --build -d ``` - Build the production environment and run it.

### Other Common Docker Commands
----

- ``` docker-compose down ``` - Stop all containers.
- ``` docker-compose -f docker-compose.yml down ``` - Stop all containers in the compose file.
- ``` docker-compose down --remove-orphans ``` - Stop all containers and delete all volumes associated with them.
- ``` docker network create supernet ``` - Create network 'supernet' if it doesn't exists.
- ``` docker system prune -af ``` - Remove all stopped containers, networks, volumes, and images.

### Application Docker Commands
----

- ``` sudo docker network create supernet ``` - Create the network manually.
- ``` sudo docker-compose --project-name=MyEmployee -f docker-compose.yml up --build -d ``` - Run the project environment.
- ``` sudo docker logs -f --tail 100 myemployee_django_1 ``` - Display django consol logs.
- ``` sudo docker exec -it myemployee_django_1 sh ``` - Access django shell.

### Backup & Restore Database
----

- ``` docker exec -t PostgreSQL pg_dumpall -c -U MyEmployeeDjangoUser > dump/dump_latest.sql ```  - Backup
- ``` cat dump/dump_latest.sql | docker exec -i PostgreSQL psql -U MyEmployeeDjangoUser ``` - Restore
