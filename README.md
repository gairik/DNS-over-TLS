

##Description

This system contains the following files:


1. client.py  
It makes a request query to the proxyserver.py. It attaches the certificate cert.pem . 
The query (b"google.com") to proxyserver.py at 127.0.0.1 on port  8443. 
The client then waits for a reply from 

2. proxyserver.py 
The proxyserver is started before the client.py, since it needs to start listening. It recieves the query from the client.py
connstream() function is used to send the query at Google DNS resolver ("8.8.8.8",53) based on TCP connection. 

3. Dockerfile - build a runtime environment for the client and server

4. key.pem and cert.pem for DNS-over-TLS encryption

5. start.sh - it will start the system and output the DNS address

6. README.md file.

#Overall Architeecture

               127.0.0.1                           |  Foreign
                                                   |
    +---------+               +----------+         |  +--------+
    |         | user queries  |          |queries  |  |        |
    |         |-------------->|          |---------|->|Foreign |
    |client.py|               | proxyser | 8.8.8.8 |  |  Name  |
    |         |<--------------| ver.py   |<--------|--| Server |
    |         | user responses|          |responses|  |        |
    +---------+               +----------+         |  +--------+
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |

##Instruction to start
This scripts assumes that Docker is pre-installed in the system and its run on Ubuntu.

Please Run the start.sh file.
./start.sh

It will do the following
1. Stop and delete any container running with name dns-over-tls 
2. Build the Dockerfile - copies all the files and runs the proxyserver
3. Runs the client.py ie the query (google.com) from local shell.
4. Output DNS result. 
