# syntax=docker/dockerfile:1.2

ARG ARCH
ARG FEDORA_VERSION
FROM fedora:${FEDORA_VERSION:-latest}

# sshd, systemd, passwordless sudo container for ansible target use etc
# docker run --privileged -d -p 2222:22 --rm --name vmlet-fedora-base

LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

ENV SSH_PORT=22
ENV SSH_USER=devops
ENV PYTHON_VERSION=38
# ENV SSH_KEY_NAME=devops

# These keys are "well known" vagrant keys - they are NOT for production use
# ENV SSH_PUBLIC_KEY_URL=https://raw.githubusercontent.com/hashicorp/vagrant/master/keys/vagrant.pub
# ENV SSH_PRIVATE_KEY_URL=https://raw.githubusercontent.com/hashicorp/vagrant/master/keys/vagrant

# 1) Install, configure, and enable sshd using *CentOS* RPM, RHEL RPM not distributable with ubi
# 2) Add a user and ssh public key 
# 3) Add EPEL? dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm && \
# 4) OPTIONAL, enable passwordless sudo   


# Configure ssh keys AND set the password 'devops' for the devops user
# Configure sshd using a typical RHEL 8.4 config

COPY ssh_config_dir_resources/* /home/${SSH_USER}/.ssh/
COPY sshd_config/*  /etc/ssh

# The SSH_USER_PASSWORD is devops but full support for ssh keys is baked in
# Configure ssh keys AND add the password 'devops' for the devops user

ENV SSH_USER_PASSWORD='$6$tWkgXG0kU57p7Rjc$ZCvOpW.oHLT0l6KEnk8CUW.o2OjP7vtnly8YbhXMd4ArugznNQFEwkpMR2S7hHLZxrjYIKFgCXLtBakh21Z4t0'


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
      systemd \
    && echo "RSAAuthentication yes" >> /etc/ssh/sshd_config \
    && echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config \
    && ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key \
    && systemctl enable --now sshd.service \
    && useradd --uid 1000 ${SSH_USER} \
    && mkdir -p /home/${SSH_USER}/.ssh \
    && chmod 600 /home/${SSH_USER}/.ssh/* \
    && chmod 700 /home/${SSH_USER}/.ssh \
    && chown -R ${SSH_USER}:${SSH_USER} /home/${SSH_USER} \
    && echo "${SSH_USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && sed -i"" "s/^devops:\!\!/devops:${SSH_USER_PASSWORD}/" /etc/shadow \
    && dnf clean all \
    && rm -rf /var/cache/dnf /root/.cache \
    && (cd /lib/systemd/system/sysinit.target.wants/ ; for i in * ; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i ; done) ; \
      rm -f /lib/systemd/system/multi-user.target.wants/* \
      rm -f /etc/systemd/system/*.wants/* \
      rm -f /lib/systemd/system/local-fs.target.wants/* \
      rm -f /lib/systemd/system/sockets.target.wants/*udev* \
      rm -f /lib/systemd/system/sockets.target.wants/*initctl* \
      rm -f /lib/systemd/system/basic.target.wants/* \
      rm -f /lib/systemd/system/anaconda.target.wants/*

EXPOSE ${SSH_PORT:-22}

#RUN systemctl enable sshd.service

COPY entrypoint.sh /entrypoint.sh

# USER devops # Fix via sudo in CMD?

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/sbin/init"]
