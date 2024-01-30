#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

# Load environment variables from .env file
set -o allexport
source $SCRIPT_DIR/../.env.example
set +o allexport

# Prompt whether or not to launch the database container using docker
read -p "Launch database container using docker? [y/n] " -n 1 -r
echo # move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
  # Start PostgreSQL container
  docker run -d \
    --name lire-db-postgres \
    -p "$DB_PORT":5432 \
    -e POSTGRES_USER="$DB_USER" \
    -e POSTGRES_PASSWORD="$DB_PASS" \
    -e POSTGRES_DB="$DB_NAME" \
    postgres:alpine3.17

  # Wait for the PostgreSQL container to be ready
  until docker exec lire-db-postgres pg_isready > /dev/null 2>&1; do
    sleep 1;
  done

  # Set environment variables for application use
  export DATABASE_URL="$DB_ENGINE://$DB_USER:$DB_PASS@$DB_HOST:$DB_PORT/$DB_NAME"
  export DEBUG="$DEBUG"
  export DJANGO_SECRET_KEY="$DJANGO_SECRET_KEY"
  export DJANGO_ALLOWED_HOSTS="$DJANGO_ALLOWED_HOSTS"

  # Copy .env.example to ./app/.env if it doesn't exist
  if [ ! -f ../app/.env ]; then
    echo "Copying .env.example to /app/.env"
    cp $SCRIPT_DIR/../.env.example $SCRIPT_DIR/../app/.env
  else
    echo "/app/.env already exists"
  fi

  # Run the migrations and start the Django development server
  python3 $SCRIPT_DIR/../app/manage.py migrate && python3 ../app/manage.py runserver

else
  echo "Make sure to setup you database before running the application."
fi