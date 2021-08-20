#!/usr/bin/env python
"""An Ansible dynamic inventory script for docker containers. This script
assumes you already have docker running on your system.

Python packages required:
- ansible>=2.1
- docker>=2.2.1

Run:
./docker_inventory.py --list
./docker_inventory.py --host my_host

Sample output:
{
    "all": {
        "hosts": ["1234"]
    },
     "_meta": {
        "hostvars": {
            "1234": {"ansible_connection": "docker"}
        }
    }
}
"""

from argparse import ArgumentParser
from copy import deepcopy
from json import dumps

from docker import DockerClient


class DockerInventory(object):
    """Docker inventory class.

    This class will generate the data structure needed by ansible inventory
    host for either all containers on your system or the one you declare. The
    data structure generated is in JSON format.
    """

    _data_structure = {'all': {'hosts': []}, '_meta': {'hostvars': {}}}

    def __init__(self, option):
        """Constructor.

        When the docker inventory class is instanticated, it performs the
        following tasks:
            * Instantiate the docker client class to create a docker object.
            * Generate the JSON data structure.
            * Print the JSON data structure for ansible to use.
        """
        self.docker = DockerClient().from_env()

        if option.list:
            data = self.containers()
        elif option.host:
            data = self.containers_by_host(option.host)
        else:
            data = self._data_structure
        print(dumps(data))

    def get_containers(self):
        """Return all docker containers on the system.

        :return: Collection of containers.
        """
        return self.docker.containers.list(all=False)

    def containers(self):
        """Return all docker containers to be used by ansible inventory host.

        :return: Ansible required JSON data structure with containers.
        """
        resdata = deepcopy(self._data_structure)
        for container in self.get_containers():
            resdata['all']['hosts'].append(container.name)
            resdata['_meta']['hostvars'][container.name] = \
                {'ansible_connection': 'docker'}

        return resdata

    def containers_by_host(self, host=None):
        """Return the docker container requested to be used by ansible
        inventory host.

        :param host: Host name to search for.
        :return: Ansible required JSON data structure with containers.
        """
        resdata = deepcopy(self._data_structure)
        for container in self.get_containers():
            if str(container.name) == host:
                resdata['all']['hosts'].append(container.name)
                resdata['_meta']['hostvars'][container.name] = \
                    {'ansible_connection': 'docker'}
                break

        return resdata


if __name__ == "__main__":
    dynamic_parser = ArgumentParser()
    dynamic_parser.add_argument('--list', action='store_true')
    dynamic_parser.add_argument('--host')

    DockerInventory(dynamic_parser.parse_args())
