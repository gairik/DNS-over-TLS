FROM python:3.6.5-alpine

RUN apk update \
  && apk upgrade \
  && rm -rf /var/cache/apk/*

RUN pip3 install dnslib    

COPY . /home/dnsproxy

WORKDIR /home/dnsproxy

ENTRYPOINT python proxyserver.py