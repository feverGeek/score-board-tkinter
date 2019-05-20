from socket import *
from threading import Thread

# 1. 收数据,然后打印
def recvData():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print('>>%s:%s' %(str(recvInfo[1]), recvInfo[0]))

# 2. 检测键盘,发数据
def sendData(sendAddr):
    while True:
        sendInfo = input('<<')
        udpSocket.sendto(sendInfo.encode('gb2312'), (destIp, destPort))

# 全局变量
udpSocket = None
destIp = ''
destPort = 0

def main():
    
    global udpSocket
    global destIp
    global destPort

    destIp = input('对方ip:')
    destPort = int(input('对方Port:'))

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('', 7788))

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    # 等子线程结束
    tr.join()
    ts.join()

if __name__ == '__main__':

    main()
