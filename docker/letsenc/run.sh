# Requires access to port 80 from the internet, adjust your firewall if needed.
docker run --rm -it \
  -v "${PWD}/docker-data/certbot/certs/:/etc/letsencrypt/" \
  -v "${PWD}/docker-data/certbot/logs/:/var/log/letsencrypt/" \
  -p 80:80 \
  certbot/certbot certonly --standalone -d  test.robointerativo.ru

