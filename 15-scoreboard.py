#!/usr/bin/env python3

from socket import *

HOST = '127.0.0.1' # or 'localhost'
PORT = 7788
BUFSIZ = 1024
ADDR = (HOST, PORT)


while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)
    # if not data:
    #     break
    print(data)


tcpCliSock.close()

