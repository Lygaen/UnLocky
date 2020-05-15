# coding:utf-8
import socket
import os
import capteurs
import motors
import random
import time
from other import Door

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

open_motor = motors.Rotation_Motor('Open')
close_motor = motors.Rotation_Motor('Close')
chock_capteur = capteurs.Tension_Capteur('Chock')
door_open = capteurs.Poussoir_Capteur('Opened')


def handle_client(conn, addr):
    try:
        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == 'quit':
                    connected = False
                elif msg == 'open':
                    os.system('cls')
                    chock_capteur.set_chock(False)
                    check = 1
                    loop_state = True
                    while loop_state:
                        if door_open.state:
                            print('Door already opened !')
                            break
                        if not open_motor.running:
                            open_motor.start()
                        if chock_capteur.got_chock(check):
                            loop_state = False
                        # Met de l'aléatoire pour si il y a un choc
                        luck = random.randint(1, 25)
                        if luck == 25:
                            chock_capteur.set_chock(True)
                        elif check == 15:  # Finis aux loop n°15
                            door_open.state == True
                            loop_state = False
                        check += 1
                        time.sleep(0.5)
                    open_motor.stop()
                    if chock_capteur.chock_state:
                        print("Door didn't open : A chock has been detected")
                    else:
                        if door_open.state:
                            pass
                        else:
                            print('Door succesfully opened !')
                            door_open.state = True
                elif msg == 'close':
                    os.system('cls')
                    chock_capteur.set_chock(False)
                    check = 1
                    loop_state = True
                    while loop_state:
                        if not door_open.state:
                            print('Door already closed !')
                            break
                        if not close_motor.running:
                            close_motor.start()
                        if chock_capteur.got_chock(check):
                            open_motor.stop()
                            loop_state = False
                        # Met de l'aléatoire pour si il y a un choc
                        luck = random.randint(1, 25)
                        if luck == 25:
                            chock_capteur.set_chock(True)
                        elif check == 15:  # Finis aux loop n°15
                            close_motor.stop()
                            door_open.state == False
                            loop_state = False
                        check += 1
                        time.sleep(0.5)
                    close_motor.stop()
                    if chock_capteur.chock_state:
                        print("Door didn't closed : A chock has been detected")
                    else:
                        if not door_open.state:
                            pass
                        else:
                            print('Door succesfully closed !')
                            door_open.state = False
        conn.close()
        os.system('cls')
        print('User quitted')
        start()
    except ConnectionResetError:
        conn.close()
        os.system('cls')
        print('User quitted')
        start()

# ConnectionResetError


def start():
    print(f'Waiting on port {PORT}')
    server.listen(1)
    conn, addr = server.accept()
    os.system('cls')
    print('Client connected !')
    handle_client(conn, addr)


print('Creating and setting up the Server...')
start()
