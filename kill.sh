echo "### Killing Docker Containers"
docker kill $(docker ps -q)
echo "### Deleting Docker Containers"
docker rm $(docker ps -a -q)
