from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 10002
ADDRESS = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('连接来自于: ', self.client_address)
        data = self.rfile.readline().strip().decode()
        print(data)
        self.wfile.write(('[%s] %s' % (ctime(), data)).encode())

tcpServer = TCP(ADDRESS, MyRequestHandler)
print('等待连接')
tcpServer.serve_forever()

