import socket
import os
import sys

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    def send(message):
        msg = message.encode(FORMAT)
        msg_length = len(msg)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(msg)

    connected = True
    while connected:
        input_ = input()
        send(input_)
        if input_ == 'quit':
            connected = False
    sys.exit()
except ConnectionRefusedError:
    os.system('cls')
    print("Il faut toujours allumer le serveur d'abord ! Sinon ça ne marche pas")
    os.system('pause>nul')
