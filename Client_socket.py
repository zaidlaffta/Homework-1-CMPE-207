# Import socket module
import socket
import sys
import os
# Create a socket object
s = socket.socket()
# Define the port on which you want to connect
port = 23
# connect to the server or remote host
s.connect(('94.142.241.111', port))
# receive data from the server
while (True):
    data = s.recv(8096)
    print(data.decode())
s.close()
