# syntax = docker/dockerfile:1.0-experimental

ARG RHEL_VERSION
FROM registry.access.redhat.com/ubi8/ubi-init:${RHEL_VERSION:-latest}

# ssh, systemd, passwordless sudo container for ansible target use etc
#
# docker run --privileged -d -p 2222:22 --rm --name vmlet-rhel-8-base

LABEL maintainer="Tok - Tony Kay tony.g.kay@gmail.com"

ENV SSH_PORT=22
ENV SSH_USER=devops
ENV PYTHON_VERSION=36
# ENV SSH_KEY_NAME=devops

# CentOS openssh-server to not break UBI restrictions

ENV SSH_SERVER_RPM=openssh-server-8.0p1-5.el8.x86_64.rpm
ENV SSH_SERVER_RPM_HOME=http://mirror.centos.org/centos/8/BaseOS/x86_64/os/Packages/

# These keys are "well known" vagrant keys - they are NOT for production use
# ENV SSH_PUBLIC_KEY_URL=https://raw.githubusercontent.com/hashicorp/vagrant/master/keys/vagrant.pub
# ENV SSH_PRIVATE_KEY_URL=https://raw.githubusercontent.com/hashicorp/vagrant/master/keys/vagrant

# 1) Install, configure, and enable sshd using *CentOS* RPM, RHEL RPM not distributable with ubi
# 2) Add a user and ssh public key 
# 3) Add EPEL? dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm && \
# 4) OPTIONAL, enable passwordless sudo   


# Configure ssh keys AND add the password 'devops' for the devops user
COPY ssh_config_dir_resources/* /home/${SSH_USER}/.ssh/

ENV SSH_USER_PASSWORD='$6$tWkgXG0kU57p7Rjc$ZCvOpW.oHLT0l6KEnk8CUW.o2OjP7vtnly8YbhXMd4ArugznNQFEwkpMR2S7hHLZxrjYIKFgCXLtBakh21Z4t0'

RUN dnf update -y \
    && rpm -Uvh http://mirror.centos.org/centos/8/BaseOS/x86_64/os/Packages/openssh-8.0p1-5.el8.x86_64.rpm \
    && rpm -Uvh ${SSH_SERVER_RPM_HOME}${SSH_SERVER_RPM} \
    && dnf install -y \
      bind-utils \
      file \
      hardlink \
      hostname \
      iputils \
      iproute \
      less \
      openssh-clients \
      python${PYTHON_VERSION:-36} \
      sudo \
    && echo "RSAAuthentication yes" >> /etc/ssh/sshd_config \
    && echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config \
    && ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key \
    && systemctl enable sshd.service \
    && useradd --uid 1000 ${SSH_USER} \
    && mkdir -p /home/${SSH_USER}/.ssh \
    && chmod 600 /home/${SSH_USER}/.ssh/authorized_keys \
    && chmod 700 /home/${SSH_USER}/.ssh \
    && chown -R ${SSH_USER}:${SSH_USER} /home/${SSH_USER} \
    && echo "${SSH_USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && sed -i"" "s/^devops:\!\!/devops:${SSH_USER_PASSWORD}/" /etc/shadow \
    && dnf clean all \
    && rm -rf /var/cache/dnf /root/.cache

EXPOSE ${SSH_PORT:-22}

COPY docker-entrypoint.sh /docker-entrypoint.sh

# USER devops # Fix via sudo in CMD?

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/sbin/init"]
