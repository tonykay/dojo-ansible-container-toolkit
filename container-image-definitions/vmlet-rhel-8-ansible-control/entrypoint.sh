#!/usr/bin/bash

cd /tmp

# Setup ssh

if [ -n "${SSH_DIR_SOURCE+set}" ]
then
  echo SSH_DIR_SOURCE is $SSH_DIR_SOURCE
  curl -L -C - -O "$SSH_DIR_SOURCE"
  tar -xf $(basename "$SSH_DIR_SOURCE")
  cp -r ./classroom/resources/bind_mounts/ssh/* /home/"${SSH_USER:-devops}"/.ssh
  chown -R ${SSH_USER}:${SSH_USER} /home/${SSH_USER}/.ssh
else
  echo SSH_DIR_SOURCE not set, use defaults or bind_mounts
fi

# rm -fr /tmp/classroom

exec "$@"
