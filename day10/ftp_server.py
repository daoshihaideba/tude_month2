"""
ftp文件服务器服务端
"""
import os
from socket import *
from threading import Thread
from time import sleep

# 文件库
FTP = "/home/tarena/FTP/"


# 自定义线程类完成客户端请求
class Handle(Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        super().__init__()

    # 处理文件列表的获取
    def do_list(self):
        files = os.listdir(FTP)  # 获取文件列表
        if files:
            self.conn.send(b"OK")
            sleep(0.1)  # 防止ＯＫ与后面内容粘连
            # 　发送文件列表 防止粘包　拼接　－》　一起发送
            data = "\n".join(files)
            self.conn.send(data.encode())
        else:
            self.conn.send(b"EMPTY")

    # 处理客户端下载  服务端： 发送文件
    def do_get(self, filename):
        try:
            fr = open(FTP + filename, 'rb')
        except:
            # 文件不存在
            self.conn.send(b"FAIL")
        else:
            self.conn.send(b"OK")
            sleep(0.1)
            # 发送文件
            while True:
                data = fr.read(1024)
                if not data:
                    break
                self.conn.send(data)
            fr.close()
            sleep(0.1)  # 防止 ## 与文件内容粘连
            self.conn.send(b"##")  # 结束标志

    def do_put(self, filename):
        # 判断文件是否已经存在
        if os.path.exists(FTP + filename):
            self.conn.send(b"EXISTS")
        else:
            self.conn.send(b"OK")
            # 接收文件
            fw = open(FTP + filename, 'wb')
            while True:
                data = self.conn.recv(1024)
                if data == b'##':
                    break
                fw.write(data)
            fw.close()

    # 具体做事情 处理客户端请求
    def run(self):
        # 循环接收客户端请求
        while True:
            request = self.conn.recv(1024)
            tmp = request.decode().split(' ')  # 解析
            if not request or tmp[0] == "QUIT":
                break # 跳出循环线程结束
            elif tmp[0] == "LIST":
                self.do_list()
            elif tmp[0] == "GET":
                self.do_get(tmp[1])  # tmp --> [GET,filename]
            elif tmp[0] == "PUT":
                self.do_put(tmp[1])  # tmp --> [PUT,filename]
        self.conn.close()


# 搭建网络
class FTPServer:
    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = self._create_socket()

    # 创建套接字  ，绑定地址
    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        return sock

    # 服务启动，可以让客户端链接
    def serve_forever(self):
        self.sock.listen(3)
        print("Listen the port %d" % self.port)
        # 循环接受连接
        while True:
            conn, addr = self.sock.accept()
            print("Connect from", addr)
            t = Handle(conn, addr)  # 创建线程
            t.start()


if __name__ == '__main__':
    ftp = FTPServer(host='0.0.0.0', port=8888)
    ftp.serve_forever()  # 启动服务
