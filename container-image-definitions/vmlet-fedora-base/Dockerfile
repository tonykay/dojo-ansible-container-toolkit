# syntax=docker/dockerfile:1.2

ARG ARCH
ARG FEDORA_VERSION
#FROM fedora-init:${FEDORA_VERSION:-latest}
FROM debock-fedora-init:latest


# sshd, systemd, passwordless sudo container for ansible target use etc
# docker run --privileged -d -p 2222:22 --rm --name vmlet-fedora-base

LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

ENV SSH_PORT=22
ENV SSH_USER=devops
ENV PYTHON_VERSION=38

# Configure ssh keys AND set the password 'devops' for the devops user
# These keys are "well known" vagrant keys - they are NOT for production use
# ENV SSH_PUBLIC_KEY_URL=https://raw.githubusercontent.com/hashicorp/vagrant/master/keys/vagrant.pub
# ENV SSH_PRIVATE_KEY_URL=https://raw.githubusercontent.com/hashicorp/vagrant/master/keys/vagrant

COPY ssh_config_dir_resources/* /home/${SSH_USER}/.ssh/
# Configure sshd using a typical RHEL 8.4 config
COPY sshd_config/*  /etc/ssh

# The SSH_USER_PASSWORD is devops but full support for ssh keys is baked in
# Configure ssh keys AND add the password 'devops' for the devops user

ENV SSH_USER_PASSWORD='$6$tWkgXG0kU57p7Rjc$ZCvOpW.oHLT0l6KEnk8CUW.o2OjP7vtnly8YbhXMd4ArugznNQFEwkpMR2S7hHLZxrjYIKFgCXLtBakh21Z4t0'

# 1) Add base packages - this image could be an ansible target so some nice to have packages
# 2) Add ssh and systemd packages
# 3) Add a user and ssh public key 
# 4) Enable passwordless sudo   

RUN rm -f /etc/yum.repos.d/fedora-cisco-openh264.repo \
    && dnf update -y \
    && dnf install -y \
      bind-utils \
      file \
      hardlink \
      hostname \
      iputils \
      iproute \
      less \
      libedit \
      ncurses \
      procps-ng \
      python${PYTHON_VERSION:-38} \
      openssh \
      openssh-clients \
      openssh-server \
      sudo \
    && ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key \
    && useradd --uid 1000 ${SSH_USER} \
    && mkdir -p /home/${SSH_USER}/.ssh \
    && chmod 600 /home/${SSH_USER}/.ssh/* \
    && chmod 700 /home/${SSH_USER}/.ssh \
    && chown -R ${SSH_USER}:${SSH_USER} /home/${SSH_USER} \
    && echo "${SSH_USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && sed -i "s/^devops:\!\!/devops:${SSH_USER_PASSWORD}/" /etc/shadow \
    && systemctl enable sshd.service \
    && dnf clean all \
    && rm -rf /var/cache/dnf /root/.cache

COPY entrypoint.sh /entrypoint.sh

# USER devops # Fix via sudo in CMD?

# RUN systemctl enable --now sshd.service 

EXPOSE ${SSH_PORT:-22}

VOLUME [ "/sys/fs/cgroup", "/tmp", "/run" ]

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/sbin/init"]
