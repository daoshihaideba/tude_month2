"""
udp 套接字客户端  udp_client.py
重点代码
"""
from socket import *

# 访问服务器需要使用的地址
ADDR = ("127.0.0.1",8888)

# 创建套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 循环发送后接收
while True:
    msg = input(">>")
    udp_socket.sendto(msg.encode(),ADDR)
    if not msg or msg == '##':
        break  # 发送给服务端之后 退出循环
    data,addr = udp_socket.recvfrom(1024)
    print("From server:",data.decode())

udp_socket.close()

