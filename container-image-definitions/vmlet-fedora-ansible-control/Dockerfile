FROM fedora:34

LABEL maintainer="Robert de Bock <robert@meinit.nl>"
LABEL build_date="2021-04-29T07:05:00Z"

# LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

ENV container=docker

# syntax = docker/dockerfile:1.0-experimental

#ARG FEDORA_VERSION
#FROM quay.io/fedora/fedora:${FEDORA_VERSION:-latest}

# ssh, systemd, passwordless sudo container for ansible target use etc
#
# docker run --privileged -d -p 2222:22 --rm --name vmlet-rhel-8-base

# Enable systemd.

ENV SSH_PORT=22
ENV SSH_USER=devops
ENV PYTHON_VERSION=38
# ENV SSH_KEY_NAME=devops

# Configure ssh keys AND add the password 'devops' for the devops user
COPY ssh_config_dir_resources/* /home/${SSH_USER}/.ssh/

ENV SSH_USER_PASSWORD='$6$tWkgXG0kU57p7Rjc$ZCvOpW.oHLT0l6KEnk8CUW.o2OjP7vtnly8YbhXMd4ArugznNQFEwkpMR2S7hHLZxrjYIKFgCXLtBakh21Z4t0'

RUN dnf -y install systemd && dnf clean all && \
  (cd /lib/systemd/system/sysinit.target.wants/ ; for i in * ; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i ; done) ; \
  rm -f /lib/systemd/system/multi-user.target.wants/* ;\
  rm -f /etc/systemd/system/*.wants/* ;\
  rm -f /lib/systemd/system/local-fs.target.wants/* ; \
  rm -f /lib/systemd/system/sockets.target.wants/*udev* ; \
  rm -f /lib/systemd/system/sockets.target.wants/*initctl* ; \
  rm -f /lib/systemd/system/basic.target.wants/* ;\
  rm -f /lib/systemd/system/anaconda.target.wants/*

RUN dnf update -y \
    && dnf install -y \
      bind-utils \
      buildah \
      file \
      hardlink \
      hostname \
      gcc \
      iputils \
      iproute \
      jq \
      less \
      libedit \
      oniguruma-devel \
      openssh \
      openssh-clients \
      openssh-server \
      ncurses \
      podman \
      python${PYTHON_VERSION:-38} \
      python3-devel \
      skopeo \
      sudo \
      vim \
    && echo "RSAAuthentication yes" >> /etc/ssh/sshd_config \
    && echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config \
    && ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key \
    && systemctl enable sshd.service \
    && useradd --uid 1000 ${SSH_USER} \
    && mkdir -p /home/${SSH_USER}/.ssh \
    && chmod 600 /home/${SSH_USER}/.ssh/* \
    && chmod 700 /home/${SSH_USER}/.ssh \
    && chown -R ${SSH_USER}:${SSH_USER} /home/${SSH_USER} \
    && echo "${SSH_USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && sed -i"" "s/^devops:\!\!/devops:${SSH_USER_PASSWORD}/" /etc/shadow 


RUN dnf install -y python3-pip \
    && pip3 --no-cache-dir install \
      ansible \
      ansible-navigator \
      ansible-builder \ 
    && pip3 cache purge 

RUN    dnf clean all \
    && rm -rf /var/cache/dnf /root/.cache

EXPOSE ${SSH_PORT:-22}

# VOLUME ["/sys/fs/cgroup"]

COPY entrypoint.sh /entrypoint.sh
COPY storage.conf /etc/containers/storage.conf

# USER devops # Fix via sudo in CMD?

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/sbin/init"]

