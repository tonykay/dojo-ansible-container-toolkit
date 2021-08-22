FROM fedora
MAINTAINER http://fedoraproject.org/wiki/Cloud

# 99.99% https://github.com/fedora-cloud/Fedora-Dockerfiles/blob/master/systemd/systemd/Dockerfile
# Cleaned style, got rid of a RUN/Layer

ENV container docker

RUN dnf -y update \
  && dnf -y install systemd \
  && dnf clean all \
  && (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
    rm -f /lib/systemd/system/multi-user.target.wants/*;\
    rm -f /etc/systemd/system/*.wants/*;\
    rm -f /lib/systemd/system/local-fs.target.wants/*; \
    rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
    rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
    rm -f /lib/systemd/system/basic.target.wants/*;\
    rm -f /lib/systemd/system/anaconda.target.wants/*;

VOLUME [ "/sys/fs/cgroup", "/tmp", "/run" ]

CMD ["/usr/sbin/init"]
