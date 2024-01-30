# Lire Back End Core
Lire is a web application that allows users to read stories and articles, follow authors, and write their own stories. This repository contains the back end core of the application. The front end web application of the application can be found in [lire-fe-web](https://github.com/HexCave/lire-fe-web) and the mobile application can be found in [lire-fe-flutter](https://github.com/HexCave/lire-fe-flutter).

## Django with Docker

The develope environment of this application is configured using Docker Compose. This readme file will guide you on how to set up and run the application.

## Prerequisites

- Docker installed on your system
- Docker Compose installed on your system
- Basic knowledge of Django

## Setup

1. Clone this repository to your local machine.
2. Navigate to the root directory of the project in your terminal.
3. Run the command `docker-compose build` to build the Docker image.
4. Run the command `docker-compose up` to start the Docker containers.

## Initiating the local runtime environment
There are two ways to run the application. Either you can run the application using docker compose or you can configure your local environment and start the application in it. The following steps will guide you through the process of setting up your local environment.

If you're using docker compose, you can run the local-dev/compose.init.sh script, which will build the docker images and collect static assets.

If you're using your local environment, you can run the local-dev/local.init.sh script, which will setup the essential environment variables and optionally setup a database using docker.

To clean up the local environment, you can run the local-dev/local.clean.sh script, which will remove the database container and the environment variables.

## Running Commands

To run Django commands, you can use the `docker-compose run` command. Here are some examples:

**To run django commands**
```sh
# Run any commands in the below documented format
docker-compose run --rm <service> sh -c 'python3 manage.py <command>'

# To make migrations
docker-compose run --rm app sh -c 'python3 manage.py makemigrations'

# To migrate
docker-compose run --rm app sh -c 'python3 manage.py migrate'

# To create a superuser
docker-compose run --rm app sh -c 'python3 manage.py createsuperuser'

# To run tests
docker-compose run --rm app sh -c 'python3 manage.py test'

# To seed the database
docker-compose run --rm app sh -c 'python3 manage.py loaddata fixture/<users/categories/stories>.json'
```

**To run the linter**
```sh
docker-compose run --rm app sh -c 'flake8'
```
## Accessing the Application

The application can be accessed at `http://localhost:8080` in your web browser.

## Stopping the Application

To stop the Docker containers, simply press `CTRL+C` in your terminal. To destroy the Docker containers, run the command `docker-compose down`.

## Deployment

To deploy the application in a non-Docker environment, you will need to set up a web server such as Nginx or Apache, and configure it to serve the Django application. You will also need to set up a database server such as MySQL or PostgreSQL and configure the Django settings to use the correct database connection settings.

## Conclusion

That's it! You should now have a fully functioning Django application running in Docker. If you have any questions or issues, feel free to open an issue on this repository.