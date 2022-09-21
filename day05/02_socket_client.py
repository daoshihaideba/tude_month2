"""
用户配合测试监听套接字链接情况
"""
from socket import *

# 访问服务器的地址
ADDR = ("127.0.0.1",8888)

# 创建tcp套接字
tcp_socket = socket()
tcp_socket.connect(ADDR)

msg = input(">>") # 阻塞