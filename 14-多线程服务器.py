#!/usr/bin/env python3
# coding=utf-8

from socket import *
from threading import Thread
from time import sleep

conNum = 0
conClientAddr = []

def dealWithClient(newSocket, destAddr):
    global conNum
    i = 0
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            if recvData.decode() == 'check':
                print('check...')
                newSocket.send(str(conNum).encode())
                for addr in conClientAddr:
                    print('send addr')
                    newSocket.send(str(addr).encode())
            print('recv[%s]:%s'%(str(destAddr), recvData))
            i+=1
            print(i)
        else:
            print('[%s]客户端关闭'%(str(destAddr)))
            i+=1
            print(i)
            break

    newSocket.close()
    

def main():

    global conNum
    global conClientAddr

    serSocket = socket(AF_INET, SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ('', 7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)

    try:
        while True:
            print('-----main process, listenning port:7788...')
            newSocket, destAddr = serSocket.accept()
            print('-----main process, processing data[%s]----'%str(destAddr))
            client = Thread(target=dealWithClient, args=(newSocket,destAddr))
            client.start()
            conNum += 1
            conClientAddr.append(destAddr)

    finally:
        serSocket.close()

if __name__ == '__main__':
    main()

