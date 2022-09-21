"""
图片上传客户端
"""
from socket import *


# 具体发送图片  读取 --》 发送
def send_image(sock):
    fr = open("/home/tarena/下载/zhao.jpeg", 'rb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        sock.send(data)
    fr.close()


def main():
    # 创建套接字，建立链接
    sock = socket()
    sock.connect(("127.0.0.1", 8888))
    send_image(sock)  # 发送图片
    sock.close()


main()
