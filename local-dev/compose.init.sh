#!/bin/bash

# This script is used to initialize the docker-compose environment.

SCRIPT_DIR=$(dirname "$0")

docker-compose -f $SCRIPT_DIR/../docker-compose.yaml build && \
docker-compose -f $SCRIPT_DIR/../docker-compose.yaml run --rm app python manage.py collectstatic --noinput