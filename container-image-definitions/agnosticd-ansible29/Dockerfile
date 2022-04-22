###  syntax # = docker/dockerfile:1.0-experimental

ARG ARCH
ARG REPO_ARCH
ARG RHEL_VERSION
FROM registry.access.redhat.com/ubi8/ubi:${RHEL_VERSION:-latest}
ENV ARCH=${ARCH:-x86_64}
ENV REPO_ARCH=${REPO_ARCH:-x86_64}

LABEL maintainer="Tony Kay - tok@redhat.com"

ENV USER=devops

# RUN dnf -y update-minimal --security --sec-severity=Important --sec-severity=Critical \
RUN dnf -y update \
    && dnf install -y \
      git \
      python${PYTHON_VERSION:-36} \
    && useradd --uid 1001 ${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && dnf clean all \
    && rm -rf /var/cache/dnf /root/.cache

RUN pip3 install --upgrade pip setuptools wheel \
    && pip3 install --upgrade "ansible<2.10"
    
COPY entrypoint-vars.sh /entrypoint.sh
RUN chmod 777 entrypoint.sh

USER devops
WORKDIR /home/devops/

RUN git clone https://github.com/redhat-cop/agnosticd.git

# WORKDIR /home/devops/agnosticd

ENTRYPOINT ["/entrypoint.sh"]

CMD ["date"]
#CMD ["ansible-playbook", "ansible/main.yml", "-e", "@/tmp/vars.yml"]