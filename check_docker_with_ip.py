# Ryuryu's Docker information script 
# -------------------------------------------
# (C) 2023 Ryan Hayabusa 
# Github: https://github.com/ryu878 
# Discord: ryuryu#4087
# Mail: ev4AR2xihu3xXcdbYy5djGpfe01@gmail.com
# Web: https://aadresearch.xyz
# Discord: ryuryu#4087
# -------------------------------------------
# python3 -m venv .docker
# source .docker/bin/activate
# pip install docker

import docker


def get_running_containers():
    client = docker.from_env()
    return client.containers.list()

def get_container_ips(container):
    networks = container.attrs['NetworkSettings']['Networks']
    return ', '.join([details['IPAddress'] for net, details in networks.items()])


if __name__ == '__main__':
    # Get running containers
    containers = get_running_containers()

    # Display the same output as 'docker ps' command, including IP addresses
    print("{:<15}  {:<40}  {:<12}  {:<25}  {:<20}".format('CONTAINER ID', 'IMAGE', 'STATUS', 'NAMES', 'IP ADDRESS'))
    for container in containers:
        print("{:<15}  {:<40}  {:<12}  {:<25}  {:<20}".format(
            container.short_id,
            container.image.tags[0] if container.image.tags else '<none>',
            container.status,
            ", ".join(container.name.split(",")),
            get_container_ips(container),
        ))
