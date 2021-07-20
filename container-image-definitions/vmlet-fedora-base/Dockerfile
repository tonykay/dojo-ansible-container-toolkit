# syntax = docker/dockerfile:1.0-experimental

ARG FEDORA_VERSION
FROM quay.io/fedora/fedora:${FEDORA_VERSION:-latest}

# ssh, systemd, passwordless sudo container for ansible target use etc
#
# docker run --privileged -d -p 2222:22 --rm --name vmlet-rhel-8-base

LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

ENV SSH_PORT=22
ENV SSH_USER=devops
ENV PYTHON_VERSION=36
# ENV SSH_KEY_NAME=devops

# Configure ssh keys AND add the password 'devops' for the devops user
COPY ssh_config_dir_resources/* /home/${SSH_USER}/.ssh/

ENV SSH_USER_PASSWORD='$6$tWkgXG0kU57p7Rjc$ZCvOpW.oHLT0l6KEnk8CUW.o2OjP7vtnly8YbhXMd4ArugznNQFEwkpMR2S7hHLZxrjYIKFgCXLtBakh21Z4t0'

RUN dnf update -y \
    && dnf install -y \
      bind-utils \
      file \
      hardlink \
      hostname \
      iputils \
      iproute \
      less \
      ncurses \
      openssh-clients \
      python${PYTHON_VERSION:-36} \
      openssh \
      sudo \
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
    && sed -i"" "s/^devops:\!\!/devops:${SSH_USER_PASSWORD}/" /etc/shadow \
    && dnf clean all \
    && rm -rf /var/cache/dnf /root/.cache

EXPOSE ${SSH_PORT:-22}

COPY entrypoint.sh /entrypoint.sh

# USER devops # Fix via sudo in CMD?

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/sbin/init"]
