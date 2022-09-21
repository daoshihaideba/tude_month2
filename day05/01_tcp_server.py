"""
tcp服务端流程

* tcp连接中当一端退出，另一端如果阻塞在recv，
此时recv会立即返回一个空字串。
* tcp连接中如果一端已经不存在，仍然试图通过
send向其发送数据则会产生BrokenPipeError
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0", 8888))

# 设置为监听套接字
tcp_socket.listen(3)

# 处理客户端连接
while True:
    print("等待客户端连接...")
    conn, addr = tcp_socket.accept()
    print("连接了：", addr)

    # 与客户端交互 ： 先收后发  -》 结束循环意味着客户端退出
    while True:
        data = conn.recv(5)
        if not data or data == b'##':
            break # 收到退出标志 或者 data 为空结束循环
        print("收到:", data.decode())
        conn.send(b"Thanks")
    conn.close()  # 与对应断开连接

# 关闭套接字
tcp_socket.close()  # 不再连接新客户端
