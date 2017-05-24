import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)
connection, client_address = sock.accept()
data =""
try:
       	while (data.count("exit")==0):
		data = connection.recv(16)
		print >>sys.stderr, 'Client: %s' % data
		connection.sendall(str(len(data)))			
finally:
        	connection.close()
		

