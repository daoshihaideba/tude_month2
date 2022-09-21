"""
http请求响应
"""
from socket import *

sock = socket()
sock.bind(("0.0.0.0",8888))
sock.listen(3)

# 等待浏览器链接
conn,addr = sock.accept()
print("Connect from",addr)

# 接收浏览器的http请求
data = conn.recv(1024)
print(data.decode())

# 组织http响应
# response = """HTTP/1.1 200 OK
# Content-Type:text/html
#
# Hello World
# """

# 字符串拼接的写法注意自己加换行格式
response = "HTTP/1.1 200 OK\r\n"
response += "Content-Type:text/html\r\n"
response += "\r\n"
response += "Hello World"
conn.send(response.encode()) # 发送响应

conn.close()
sock.close()