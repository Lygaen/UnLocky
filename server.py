# coding:utf-8
import socket
import threading
import os

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == 'quit':
                connected = False
            else:
                print(msg)
    conn.close()
    print('User quitted')


def start():
    print(f'Waiting on port {PORT}')
    server.listen(1)
    while True:
        conn, addr = server.accept()
        os.system('cls')
        print('Got new connection !')
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


print('Creating and setting up the Server...')
start()
