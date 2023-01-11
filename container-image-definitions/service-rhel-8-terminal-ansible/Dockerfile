# syntax = docker/dockerfile:1.0-experimental

FROM docker.io/tonykay/service-rhel-8-terminal-base

# Install latest ansible 2.9 version

ENV ANSIBLE_VERSION="<2.10"

LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

USER root

RUN pip3 --no-cache-dir install ansible${ANSIBLE_VERSION} \
    && yum clean all \
    && rm -rf /var/cache/yum

EXPOSE 8080

USER devops

CMD ["butterfly.server.py", "--port=8080", "--host=0.0.0.0", "--unsecure", "--i-hereby-declare-i-dont-want-any-security-whatsoever"]
