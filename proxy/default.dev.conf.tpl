server {
    listen $LISTEN_PORT;

    access_log  /var/log/nginx/access.log;
    error_log   /var/log/nginx/error.log debug;
    client_max_body_size 100M;

    location /ws/ {
        proxy_pass http://app:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
    }

    location /static {
        alias /vol/static/;
    }

    location / {
        proxy_pass              http://$APP_HOST:$APP_PORT;
        client_max_body_size    10M;
    }
}
