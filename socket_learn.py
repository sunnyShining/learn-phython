from socket import *
from time import ctime

HOST = 'localhost'
PORT = 10001
BUFFER = 1024
ADDRESS = (HOST, PORT)

serverSocket = socket(AF_INET, SOCK_STREAM) # 数据来源于socket包
serverSocket.bind(ADDRESS)

serverSocket.listen(5)

while True:
    print('等待连接')
    clientSocket, add = serverSocket.accept() # 阻塞
    print('来自: ',add)
    while True:
        data = clientSocket.recv(BUFFER).decode()
        print('来自客户端消息: ', data)
        if not data:
            break;
        clientSocket.send(('[%s] %s'%(ctime(), data)).encode())
    clientSocket.close()

serverSocket.close()