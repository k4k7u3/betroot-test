import socket

IP = "127.0.0.1"
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print("Start server")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Recieve message: {data} from {addr}")
