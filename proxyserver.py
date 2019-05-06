from dnslib import *
from dnslib import server
import ssl
import socket
import threading

server_addr = ('127.0.0.1', 8443)


context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain('cert.pem', 'key.pem')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8443))
s.listen(10)

print ("Starting Proxy Server")

while True:
    newsocket, fromaddr = s.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        #connstream.send(b"Hello World!")
        ss = connstream.recv(100)
        query = DNSRecord.question(ss)
        data = query.send("8.8.8.8",53)
        #print DNSRecord.parse(data)
        
        if len(ss)!=0 :
            connstream.send(bytes(str(DNSRecord.parse(data).rr[0].rdata), encoding='utf-8'))
    finally:
        connstream.close()


