#!/usr/bin/bash

cd ~devops/agnosticd

ansible-playbook ansible/main.yml -e @ansible/configs/test-empty-config/sample_vars.yml

#exec "$@"
