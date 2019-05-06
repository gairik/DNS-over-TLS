import ssl
import socket
import threading
import pprint

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)  #socket creation to manage certificate
context.load_verify_locations('cert.pem')
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
ssl_sock = context.wrap_socket(s, server_hostname="127.0.0.1")
ssl_sock.connect(('127.0.0.1', 8443))

ssl_sock.send(b"google.com")

print ("##################")
print ("##################")
print ("###  received from DNS-Proxy ####")
print(ssl_sock.recv(100))
print ("##################")

