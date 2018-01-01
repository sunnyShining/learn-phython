from socket import *
from time import ctime

HOST = 'localhost'
PORT = 10001
BUFFER = 1024
ADDRESS = (HOST, PORT)

udpclient = socket(AF_INET, SOCK_DGRAM)


while True:
    data = input('> ')
    if not data:
        break
    udpclient.sendto(data.encode(), ADDRESS)
    data, ADDRESS = udpclient.recvfrom(BUFFER)
    if not data:
        break
    print(data.decode())
    print(ADDRESS)

udpclient.close()