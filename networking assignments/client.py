import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
sock.connect(server_address)
try:
    message=""
    # Send data
    while(message.count("exit")==0):
	message=raw_input().strip()
    	sock.sendall(message)
	# Look for the response
        data = sock.recv(4096)
        print >>sys.stderr, 'Server Echo:  "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
