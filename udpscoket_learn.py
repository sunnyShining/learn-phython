from socket import *
from time import ctime

HOST = 'localhost'
PORT = 10001
BUFFER = 1024
ADDRESS = (HOST, PORT)

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(ADDRESS)

while True:
    print('等待信息')
    data, addr = udpSocket.recvfrom(BUFFER)
    print(data.decode())
    udpSocket.sendto(('[%s] %s' % (ctime(), data.decode())).encode(), addr)
    print('返回给: ', addr)

udpSocket.close()