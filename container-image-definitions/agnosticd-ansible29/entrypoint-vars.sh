#!/usr/bin/env bash

#[ ! -t 0 ] && cat - > /tmp/vars.yml || echo empty


#[ test -s /dev/stdin ] && echo 'pipe has data' || echo 'pipe is empty' 

#if read -t 0
#then
#  cat - > /tmp/vars.yml
#fi

#cat - > /tmp/vars.yml

#if [ -f /tmp/vars.yml ] 
if read -t 0
then
  cat - > /tmp/vars.yml
else
  cd agnosticd
  ansible-playbook ansible/main.yml -e @ansible/configs/test-empty-config/sample_vars.yml
fi
#cd ~devops/agnosticd


# exec "$@"
