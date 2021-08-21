#!/usr/bin/env python

import pyfscache
import argparse
import subprocess
try:
    import json
except ImportError:
    import simplejson as json

cache_it = pyfscache.FSCache('/tmp/docker-machine-inventory-cache', minutes = 1)

class SetEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, set):
              return list(obj)
        return json.JSONEncoder.default(self, obj)


class DockerMachineCommand:
    
    def __run_command(self, *args):
        return subprocess.check_output(["docker-machine"] + list(args)).strip()

    def inspect(self, machine_name, format):
        return self.__run_command("inspect", "-f", format, machine_name)

    def status(self, machine_name):
        return self.__run_command("status", machine_name)

    def list_names(self):
        return self.__run_command("ls", "-q").splitlines()

class SSHConfig:
    def __init__(self, user, port, key_file):
        self.user = user
        self.port = port
        self.key_file = key_file


class Host:
    def __init__(self, name, ip_address, ssh_config, groups):
        self.name = name
        self.ip_address = ip_address
        self.ssh_config = ssh_config
        self.groups = groups


class DockerMachineInventoryApplication:

    def __init__(self):
        self.dm = DockerMachineCommand()

    def __reduce_hosts_to_inventory(self, inventory, host):
        inventory.setdefault("_meta", {}).setdefault("hostvars", {})[host.name] = {
            "ansible_host": host.ip_address,
            "ansible_ssh_user": host.ssh_config.user,
            "ansible_ssh_port": host.ssh_config.port,
            "ansible_ssh_private_key_file": host.ssh_config.key_file
        };
        inventory.setdefault("all", {}).setdefault("children", set()).update(host.groups)
        inventory["all"].setdefault("hosts", set()).add(host.name)
        for group in host.groups:
           inventory.setdefault(group, {}).setdefault("hosts", set()).add(host.name)
        return inventory

    def __build_inventory(self, hosts):
        return reduce(self.__reduce_hosts_to_inventory, hosts, {})

    def __load_args(self):
        parser = argparse.ArgumentParser(description='Produce an Ansible Inventory file based on Docker Machine status')
        parser.add_argument('--list', action='store_true', help='List all active Droplets as Ansible inventory (default: True)')
        self.args = parser.parse_args()

    @cache_it
    def __get_host(self, name):
        ssh_config = SSHConfig(
            user = self.dm.inspect(name, "{{.Driver.SSHUser}}"),
            port = self.dm.inspect(name, "{{.Driver.SSHPort}}"),
            key_file = self.dm.inspect(name, "{{.Driver.SSHKeyPath}}")
        )
        return Host(
            name = name,
            ip_address = self.dm.inspect(name, "{{.Driver.IPAddress}}"),
            ssh_config = ssh_config,
            groups = [
                group for group in [
                    self.dm.inspect(name, "{{.DriverName}}")
                ] if group is not None
            ]
        )

    def __get_hosts(self):
        names = self.dm.list_names()
        return map(self.__get_host, names)

    def run(self):
        self.__load_args()
        hosts = self.__get_hosts()
        print json.dumps(self.__build_inventory(hosts), cls=SetEncoder)

DockerMachineInventoryApplication().run()
