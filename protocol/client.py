import socket
 
clients=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
clients.connect(('127.0.0.1',1234))
 
clients.send("hello server".encode())
 
recv=clients.recv(1024).decode()
print(f"server says {recv}")
 
clients.close()
