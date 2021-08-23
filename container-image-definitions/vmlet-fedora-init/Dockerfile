# syntax=docker/dockerfile:1.2
ARG ARCH

FROM fedora:latest

LABEL maintainer="Robert de Bock <robert@meinit.nl>"

ENV container=docker

# Enable systemd.
RUN rm -f /etc/yum.repos.d/fedora-cisco-openh264.repo \
  && dnf update -y \
  && dnf -y install systemd \
  && dnf clean all \
  && rm -rf /var/cache/dnf /root/.cache \
  && (cd /lib/systemd/system/sysinit.target.wants/ ; for i in * ; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i ; done) ; \
      rm -f /lib/systemd/system/multi-user.target.wants/* ;\
      rm -f /etc/systemd/system/*.wants/* ;\
      rm -f /lib/systemd/system/local-fs.target.wants/* ; \
      rm -f /lib/systemd/system/sockets.target.wants/*udev* ; \
      rm -f /lib/systemd/system/sockets.target.wants/*initctl* ; \
      rm -f /lib/systemd/system/basic.target.wants/* ;\
      rm -f /lib/systemd/system/anaconda.target.wants/*

VOLUME ["/sys/fs/cgroup"]

CMD ["/sbin/init"]
