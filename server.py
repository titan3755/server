import socket
import time
import sys


def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
        print('Socket created successfully!')
    except socket.error as msg:
        print(f'An error has occurred while creating the socket! : {msg}')


def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host, port))
        s.listen(5)
        print('Socket binded successfully!')
    except socket.error as msg:
        print(f'An error has occurred while binding the socket! : {msg}')


def accept_connection():
    global host
    global port
    global s
    conn, address = s.accept()
    print(f'Connections established successfully! IP: {address[0]} Port: {address[1]}')
    print(f'connection: {conn} address: {address}\n')
    print('-----------------------------------------------------------------\n')
    send_commands(conn)


def send_commands(conn):
    while True:
        msg = input('Enter a message > ')
        if len(str.encode(msg)) > 0:
            conn.send(str.encode(msg))
        client_response = str(conn.recv(1024), 'utf8')
        if client_response == 'close':
            conn.close()
        else:
            print(f'Message Received: {client_response}')


def main():
    create_socket()
    bind_socket()
    accept_connection()


main()
