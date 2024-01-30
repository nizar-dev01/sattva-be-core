#!/bin/bash
SCRIPT_DIR=$(dirname "$0")

rm $SCRIPT_DIR/../app/.env
# stop the docker container mypostgres if it is running
docker container ls | grep mypostgres && docker stop mypostgres