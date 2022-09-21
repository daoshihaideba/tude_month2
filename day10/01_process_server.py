"""
基于多进程的网络并发模型
"""
from multiprocessing import Process
from socket import *

# 　服务端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 具体处理客户端请求
def handle(conn,addr):
    # 与客户端配合
    while True:
        data = conn.recv(1024)
        if not data or data == b'##':
            break
        print(data.decode())
        conn.send(b"OK")
    conn.close()

# 入口函数搭建网络
def main():
    # 创建出监听套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(3)
    print("Listen the port %d"%PORT)
    #　接收客户端连接请求
    while True:
        conn,addr = sock.accept()
        print("Connect from",addr)
        # 为客户端创建新的子进程
        p = Process(target=handle,args=(conn,addr))
        p.start()


if __name__ == '__main__':
    main()
