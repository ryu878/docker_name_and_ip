# Docker information script
Python script to show running docker containers with corresponding ip addresses

I'm tired of this:
<code>docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' CONTAINER_ID</code>

So I've created python script that shows all the data same if you type
<code>docker ps</code>
and also it shows the ip address as well


![image](https://github.com/ryu878/docker_name_and_ip/assets/81808867/6e718914-47c3-4cd2-a475-c913a54990d5)
