"""
udp 服务端示例  udp_server.py
重点代码
"""
import socket

# 创建udp套接字
udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0", 8888))

# 循环先收后发
while True:
    data,addr = udp_socket.recvfrom(1024)
    # 服务器端程序有时会长期执行不结束
    # if not data or data == b"##":
    #     break # 得到客户端通知退出循环
    print(addr,":",data.decode()) # data -> byte
    udp_socket.sendto(b"Thanks",addr)

# 关闭套接字
udp_socket.close()
