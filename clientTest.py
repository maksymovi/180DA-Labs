import socket

import sys

ip_addr = sys.argv[1]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_addr, 8080))
client.send("I am CLIENT\n".encode())
from_server = client.recv(4096)
client.close()
print(from_server.decode())
