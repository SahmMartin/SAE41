#!/bin/bash

container_name="WEB"
container_id=$(docker inspect -f '{{.Id}}' "$container_name")
echo "IP $container_name : $container_id"

docker stop $container_id

docker start WEB