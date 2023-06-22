#!/bin/bash

container_name="bdd"
ip_address=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$container_name")
echo "IP $container_name : $ip_address"

echo $ip_address > 1.txt