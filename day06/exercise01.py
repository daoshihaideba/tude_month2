"""
利用tcp套接字写一个服务端http程序，将一张图片显示到浏览器中

即启动程序后浏览器访问 "127.0.0.1:8888"就可以展示出这个图片
并且浏览器可以重复的访问

响应头 ： Content-Type:image/jpeg
"""
from socket import *

# 完成一次与浏览器交互
def handle(conn):
    data = conn.recv(1024)
    print(data.decode())
    # 获取图片内容 --》 响应体
    with open(r"RISE with SAP Wallpaper 1.png",'rb') as fr:
        data = fr.read()
    response = b"HTTP/1.1 200 OK\r\n"
    response += b"Content-Type:image/png\r\n"
    response += b"\r\n"
    response += data
    conn.send(response)  # 发送响应

def main():
    sock = socket()
    sock.bind(("0.0.0.0",6660))
    sock.listen(3)

    # 等待浏览器访问
    while True:
        conn,addr = sock.accept()
        print("Connect from",addr)
        handle(conn) # 用于与浏览器交互
        conn.close()
    sock.close()

main()