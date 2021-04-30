# syntax = docker/dockerfile:1.0-experimental

FROM registry.access.redhat.com/ubi8/ubi:${RHEL_VERSION:-latest}
#FROM vmlet-rhel-8-base

LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

RUN yum install -y python3 \
    && python3 -m pip install --upgrade pip setuptools wheel \
    && pip3 --no-cache-dir install butterfly \
    && yum clean all \
    && rm -rf /var/cache/yum /root/.cache

EXPOSE 8080

USER devops
WORKDIR /home/devops

CMD ["butterfly.server.py", "--port=8080", "--host=0.0.0.0", "--unsecure", "--i-hereby-declare-i-dont-want-any-security-whatsoever"]
