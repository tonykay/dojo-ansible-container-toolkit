# syntax = docker/dockerfile:1.0-experimental

# ARG RHEL_VERSION
#FROM registry.access.redhat.com/ubi8/ubi-init:${RHEL_VERSION:-latest}


FROM quay.io/tonykay/vmlet-rhel-8-base:latest 

#vmlet-rhel-8-base
# ssh, systemd, passwordless sudo container for ansible target use etc
#
# docker run --privileged -d -p 2222:22 --rm --name vmlet-rhel-8-base

LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

ENV ANSIBLE_VERSION=<2.10
ENV SSH_PORT=22
ENV SSH_USER=devops
# ENV SSH_KEY_NAME=devops

RUN dnf install -y \
      git \
      vim \
    && python3 -m pip install --upgrade pip setuptools wheel \
    && pip3 --no-cache-dir install ansible${ANSIBLE_VERSION} \
    && pip3 cache purge \
    && dnf clean all \
    && rm -rf /var/cache/dnf /root/.cache

EXPOSE ${SSH_PORT:-22}

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/sbin/init"]
