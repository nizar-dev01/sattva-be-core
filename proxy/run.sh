#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl '$APP_HOST$APP_PORT$LISTEN_PORT' > /etc/nginx/conf.d/default.conf
nginx -g "daemon off;"