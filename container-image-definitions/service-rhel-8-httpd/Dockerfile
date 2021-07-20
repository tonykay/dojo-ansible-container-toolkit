# syntax = docker/dockerfile:1.0-experimental

# ARG RHEL_VERSION

FROM registry.redhat.io/rhel8/httpd-24
LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

ENV HTTP_PORT=80

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["run-httpd"]
