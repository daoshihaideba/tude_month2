"""
基于线程的并发模型
"""
from socket import *
from threading import Thread

# 自定义线程类完成客户端请求
class Handle(Thread):
    def __init__(self,conn,addr):
        self.conn = conn
        self.addr = addr
        super().__init__()

    # 具体做事情
    def run(self):
        # 与客户端配合
        while True:
            data = self.conn.recv(1024)
            if not data or data == b'##':
                break
            print(data.decode())
            self.conn.send(b"OK")
        self.conn.close()

# 搭建网络
class TCPServer:
    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.sock = self._create_socket()

    # 创建套接字  ，绑定地址
    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        return sock

    # 服务启动，可以让客户端链接
    def serve_forever(self):
        self.sock.listen(3)
        print("Listen the port %d"%self.port)
        # 循环接受连接
        while True:
            conn,addr = self.sock.accept()
            print("Connect from",addr)
            t = Handle(conn,addr) #创建线程
            t.start()



if __name__ == '__main__':
    server = TCPServer(host='0.0.0.0', port=8888)
    server.serve_forever()  # 启动服务
