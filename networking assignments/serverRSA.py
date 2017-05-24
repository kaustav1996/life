import socket
import sys
import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def generate_keypair(p, q):
    n = p * q

    
    phi = (p-1) * (q-1)

    
    e = random.randrange(1, phi)

    
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    
    d = multiplicative_inverse(e, phi)
    
    
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    
    key, n = pk
    
    cipher = [(ord(char) ** key) % n for char in plaintext]
    
    return cipher

def decrypt(pk, ciphertext):
    
    key, n = pk
    
    plain = [chr((char ** key) % n) for char in ciphertext]
  
    return ''.join(plain)
    
if __name__ == '__main__':
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', 10000)
	print >>sys.stderr, 'starting up on %s port %s' % server_address
	sock.bind(server_address)
	sock.listen(1)
	connection, client_address = sock.accept()
	try:
			connection.sendall("Enter a prime number (17, 19, 23, etc)")
			p=int(connection.recv(256))
			connection.sendall("Enter another prime number (Not one you entered above): ")
			q=int(connection.recv(256))
			public, private = generate_keypair(p, q)
			connection.sendall("Your public key is "+str(public)+" and your private key is "+str(private)+"..press enter")
			connection.sendall("Enter a message to encrypt with your private key: ")
			message=connection.recv(256)
			encrypted_msg = encrypt(private, message)
			connection.sendall(''.join(map(lambda x: str(x), encrypted_msg))+"...press enter")
			connection.sendall("Decrypting message with public key "+str(public)+"...press enter")
			connection.sendall("your message is " +decrypt(public, encrypted_msg)+"...type exit")
			exit_command=""
			while(exit_command!="exit"):
				exit_command=connection.recv(256)
			print("client disconnected!! closing server...")
	finally:
        	connection.close()
		

