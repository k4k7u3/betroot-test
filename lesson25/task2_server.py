import socket

IP = "127.0.0.1"
PORT = 65432

not_letter = ["!", ".", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", " "]
dictionary = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        8: "h",
        9: "i",
        10: "j",
        11: "k",
        12: "l",
        13: "m",
        14: "n",
        15: "o",
        16: "p",
        17: "q",
        18: "r",
        19: "s",
        20: "t",
        21: "u",
        22: "v",
        23: "w",
        24: "x",
        25: "y",
        26: "z"}
key = 3


def cesar(input_str: str) -> str:
    pass_str = ""
    input_str = input_str.lower()
    for item in input_str:
        if item in not_letter:
            pass_str += item
            continue
        for j in dictionary:
            if item == dictionary[j]:
                number_of_letter = j + key
                if number_of_letter > 26:
                    number_of_letter -= 26
                pass_str += dictionary[number_of_letter]
    return pass_str


sock = socket.socket()
sock.bind((IP, PORT))
sock.listen(1)

while True:
    con, addr = sock.accept()
    try:
        print(f"Connection with {addr}")
        key = con.recv(256)
        key = int(key)
        con.sendall(bytes("it was a key", encoding="utf-8"))
        data = con.recv(256)
        data_with_key = cesar(str(data))
        if data:
            con.sendall(bytes(data_with_key, encoding="utf-8"))
        else:
            print("No data")
            break
    finally:
        con.close()
