import socket

i = 0

IP = "127.0.0.1"
PORT = 65432

message = b"Hello UPD"


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(10):
    sock.sendto(message, (IP, PORT))
