# Docker information script
Python script to show running docker containers information, including IP addresses

# Why
I'm tired of this:

<code>docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' CONTAINER_ID</code>

So I've created python script that displays the same output as <code>docker ps</code> command, including IP addresses

![image](https://github.com/ryu878/docker_name_and_ip/assets/81808867/6e718914-47c3-4cd2-a475-c913a54990d5)

# How to run
1. Create virtual environment using the command
   <code>python3 -m venv .docker</code>
2. Activate it
  <code>source .docker/bin/activate</code>
3. Install the Docker SDK for Python
   <code>pip install docker</code>
4. Run with command <code>python3 check_docker_with_ip.py</code>


## Contacts
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me:

Discord: https://discord.gg/zSw58e9Uvf

Telegram: https://t.me/aadresearch

## VPS for bots and scripts
I prefer using DigitalOcean. 
To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04
