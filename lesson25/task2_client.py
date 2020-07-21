import socket

IP = "127.0.0.1"
PORT = 65432
key = "5"
msg = "Hello my dear world"

sock = socket.socket()
sock.connect((IP, PORT))
sock.sendall(bytes(key, encoding="utf-8"))
data1 = sock.recv(256)
print(data1)
sock.sendall(bytes(msg, encoding="utf-8"))
data = sock.recv(256)
print(f"Encrypted message = {str(data)}")
sock.close()
