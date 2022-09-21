"""
监听套接字链接测试
1. listen 客户端就可以链接了
2. accept是处理链接，accept 才表示链接完成
3. 监听套接字确实是可以同时连上多个客户端的
"""
from socket import *

# 创建监听套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(("0.0.0.0", 8888))
tcp_socket.listen(3)

input(">>") # 阻塞

# 处理客户端连接
while True:
    print("等待客户端连接...")
    conn, addr = tcp_socket.accept()
    print("连接了：", addr)