"""
粘包问题发送端
* 连续的发送  --》 发送的很快 接收的可能慢
解决 ： 1. 发送的慢一点 -》 发送延迟
       2. 设置固定格式的消息包
"""
from socket import *
from time import sleep

sock = socket()
sock.connect(("127.0.0.1",8880))

# 发送增加时间间隔
# sock.send(b"Lily")
# sleep(0.1)
# sock.send(b"ab123")

# 约定好格式或者结束标志
# sock.send(b"Lily#")
# sock.send(b"ab123#")

data = [
  "张三  18   177",
  "李四  19   180",
  "王五  120  183"
]
for row in data:
    sleep(0.1)
    sock.send(row.encode())


sock.close()