"""
粘包问题接收端
"""

from socket import *

# 创建监听套接字
sock = socket()
sock.bind(("0.0.0.0",8880))
sock.listen(3)
conn,addr = sock.accept() # 连接

# data = conn.recv(128).decode()
# print("User:",data)
# data = conn.recv(128).decode()
# print("Passwd:",data)

while True:
    row = conn.recv(1024)
    if not row:
        break
    print(row.decode())

conn.close()
sock.close()