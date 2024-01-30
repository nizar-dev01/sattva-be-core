FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="nizar"

COPY ./default.dev.conf.tpl /etc/nginx/default.conf.tpl
COPY ./run.sh /run.sh

ENV LISTEN_PORT=80
ENV APP_HOST=app
ENV APP_PORT=8000

USER root

RUN mkdir -p /vol && \
    chmod 755 /vol && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol

USER nginx

CMD ["/run.sh"]