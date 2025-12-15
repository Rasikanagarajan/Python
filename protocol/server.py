import socket
 
servers=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
servers.bind(('127.0.0.1',1234))
 
servers.listen()
print("server is running on 1234")
 
conm,add=servers.accept()
print(f"conneted by {add}")
 
data=conm.recv(1024).decode()
print(f"client says {data}")
 
conm.send("hello client ".encode())
conm.close()
servers.close()
