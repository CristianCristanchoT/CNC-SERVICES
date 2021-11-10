echo "### Docker Compose up"
docker-compose -f docker-compose.prod.yaml up -d --build
echo "### Changing permissions "
chmod -R go+w mongo/DB_DATA
