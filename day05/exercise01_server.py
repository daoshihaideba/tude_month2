"""
练习 1：
编写一组程序，从客户端将一张指定的图片上传到服务端，传输完成后
客户端自动结束即可，服务端接收图片 命名为 20220327.jpeg
接受完成 客户端退出服务端 if not data 也结束即可。
plus : 假设图片不确定大小，可能很大

思路 ： 客户端读取发送   服务端接收写入
"""
from socket import *


# 接收图片的具体函数
def recv_image(conn):
    fw = open("20220327.jpeg", 'wb')
    # 收图片内容 -》 写入到文件
    while True:
        data = conn.recv(1024)
        if not data:
            break
        fw.write(data)
    fw.close()


# 搭建基本的网络
def main():
    # 创建出监听套接字
    sock = socket()
    sock.bind(("0.0.0.0", 8888))
    sock.listen(3)
    # 建立链接
    conn, addr = sock.accept()
    print("Connect from", addr)
    recv_image(conn)  # 接受图片函数
    conn.close()
    sock.close()


main()
