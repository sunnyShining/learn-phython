from socket import *

HOST = 'localhost'
PORT = 10001
BUFFER = 1024
ADDRESS = (HOST, PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDRESS)
while True:
    data = input('>')
    if not data:
        break
    clientSocket.send(data.encode())
    data = clientSocket.recv(BUFFER).decode()
    if not data:
        break
    print(data)
clientSocket.close() 