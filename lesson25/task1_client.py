import socket

i = 0

IP = "127.0.0.1"
PORT = 65432

message = "Hello UPD"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while i < 10:
    sock.sendto(bytes(message, encoding='utf-8'), (IP, PORT))
    i += 1
