# Docker information script
Python script to show running docker containers with corresponding ip addresses

<code>docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' CONTAINER_ID</code>
