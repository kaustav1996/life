import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)
try:
        message=""
        while(message.count("exit")==0):
            message=raw_input().strip()
            sock.sendall(message)
            data = sock.recv(4096)
            print("Server Echo:  "+ data)

finally:
        print ("closing socket")
        sock.close()
