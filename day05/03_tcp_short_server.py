"""
tcp服务端  短连接
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0", 8888))

# 设置为监听套接字
tcp_socket.listen(3)

# 处理客户端连接 与客户端交互
while True:
    conn, addr = tcp_socket.accept()
    data = conn.recv(1024)
    print(addr,":", data.decode())
    conn.send(b"Thanks")
    conn.close()

# 关闭套接字
tcp_socket.close()  # 不再连接新客户端
