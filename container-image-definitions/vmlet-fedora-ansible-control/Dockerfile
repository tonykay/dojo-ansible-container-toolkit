FROM vmlet-fedora-base


LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

ENV container=docker

# syntax = docker/dockerfile:1.0-experimental

RUN dnf install -y \
      buildah \
      gcc \
      jq \
      oniguruma-devel \
      podman \
      procps-ng \
      python3-devel \
      python3-pip \
      skopeo \
      sudo \
      vim \
    && pip3 --no-cache-dir install \
      ansible \
      ansible-navigator \
      ansible-builder \ 
    && pip3 cache purge \
    && dnf clean all \
    && rm -rf /var/cache/dnf /root/.cache 

EXPOSE ${SSH_PORT:-22}

# VOLUME ["/sys/fs/cgroup"]

COPY entrypoint.sh /entrypoint.sh
COPY storage.conf /etc/containers/storage.conf

# USER devops # Fix via sudo in CMD?

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/sbin/init"]
