docker stop dns-over-tls || true && docker rm dns-over-tls || true

docker build . -t n26

docker run -d --name dns-over-tls n26 

docker exec -it dns-over-tls python client.py
