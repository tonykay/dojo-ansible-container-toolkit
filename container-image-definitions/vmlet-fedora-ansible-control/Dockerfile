# syntax=docker/dockerfile:1.2

FROM vmlet-fedora-base

LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

ENV container=docker

RUN dnf install -y \
      buildah \
      gcc \
      jq \
      oniguruma-devel \
      podman \
      python3-devel \
      python3-pip \
      skopeo \
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
VOLUME [ "/sys/fs/cgroup", "/tmp", "/run" ]


COPY entrypoint.sh /entrypoint.sh
COPY storage.conf /etc/containers/storage.conf

# USER devops # Fix via sudo in CMD?

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/sbin/init"]
