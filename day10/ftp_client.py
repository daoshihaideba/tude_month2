"""
ftp文件服务器客户端
"""
import sys
from socket import *
from time import sleep

# 访问服务器的地址
ADDR = ("121.5.90.43", 8888)


# 具体逻辑处理
class Handle:
    def __init__(self):
        self.sock = self._connect()

    # 　链接服务器
    def _connect(self):
        sock = socket()
        sock.connect(ADDR)
        return sock

    def do_list(self):
        self.sock.send(b'LIST')  # 发送请求
        res = self.sock.recv(128)  # 接收结果
        if res == b'OK':
            # 　接收文件列表
            files = self.sock.recv(1024 * 1024)
            print(files.decode())
        else:
            print("文件库为空！")

    # 下载  客户端接收
    def do_get(self, filename):
        msg = "GET " + filename
        self.sock.send(msg.encode())  # 发送请求
        res = self.sock.recv(128)  # 接收响应
        if res == b'OK':
            # 接收文件
            fw = open(filename, 'wb')
            while True:
                data = self.sock.recv(1024)
                if data == b'##':
                    break
                fw.write(data)
            fw.close()
        else:
            print("要下载的文件不存在")

    # 上传  客户端 发送文件
    def do_put(self, filename):
        try:
            fr = open(filename, 'rb') #防止要上传的文件不存在
        except:
            print("要上传的文件不正确！")
            return
        filename = filename.split('/')[-1] #　提取真实的文件名
        msg = "PUT " + filename
        self.sock.send(msg.encode())  # 发送请求
        res = self.sock.recv(128)  # 接收响应
        if res == b'OK':
            while True:
                data = fr.read(1024)
                if not data:
                    break
                self.sock.send(data)
            fr.close()
            sleep(0.1)  # 防止 ## 与文件内容粘连
            self.sock.send(b"##")  # 结束标志
        else:
            print("要上传的文件已存在")

    def do_quit(self):
        self.sock.send(b"QUIT")
        self.sock.close()
        sys.exit("谢谢使用")  # 结束进程


# 图形展示
class FTPView:
    def __init__(self):
        self.control = Handle()

    def _menu(self):
        print("""
        =============== FTP文件服务器 ==============
         1.查看文件库　2.下载文件　3.上传文件　4.退出
        ============================================ 
        """)

    def _select(self):
        cmd = input("请输入选项:")
        if cmd == '1':
            self.control.do_list()
        elif cmd == '2':
            filename = input("输入要下载的文件名:")
            self.control.do_get(filename)
        elif cmd == '3':
            filename = input("输入要上传的文件名:")
            self.control.do_put(filename)
        elif cmd == '4':
            self.control.do_quit()
        else:
            print("请输入正确选项！")

    def main(self):
        while True:
            self._menu()
            self._select()


if __name__ == '__main__':
    ftp = FTPView()
    ftp.main()
