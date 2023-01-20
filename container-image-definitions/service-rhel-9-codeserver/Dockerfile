# syntax = docker/dockerfile:1.0-experimental

FROM registry.access.redhat.com/ubi9/ubi-init:${RHEL_VERSION:-latest}

LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

RUN dnf install -y https://github.com/coder/code-server/releases/download/v4.4.0/code-server-4.4.0-arm64.rpm \
    && useradd devops \
    && yum clean all \
    && rm -rf /var/cache/yum /root/.cache

EXPOSE 8080

USER devops
WORKDIR /home/devops

CMD ["code-server"]
# systemctl", "start", "code-server"]
