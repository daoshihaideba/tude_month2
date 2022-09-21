"""
完成一个对话小程序，客户端可以发送问题给服务端，服务端接收到问题将对
应答案给客户端，客户端打印出来要求可以同时多个客户端提问，如果问题没
有指定答案，则回答 “人家还小，不知道。”

注意：在服务端用字典表示关键字和答案之间的对应关系即可
{"key":"value"}
key: 几岁
value ： 我2岁啦
"""
from socket import *

# 关键词与问题的对应关系
chat = {
    "几岁": "我两岁啦",
    "叫什么": "我叫小美",
    "男生女生": "我是机器人",
    "你好": "你好啊",
    "快递": "我来帮你查查"
}

# 通过问题找答案
def find_answer(question):
    # 遍历字典
    for key,value in chat.items():
        if key in question:
            return value
    return "人家还小，不知道啦！"


def main():
    # 创建监听套接字
    sock = socket()
    sock.bind(("0.0.0.0",8888))
    sock.listen(5)
    # 循环处理客户端问题
    while True:
        conn,addr = sock.accept()
        q  = conn.recv(1024)
        answer = find_answer(q.decode()) # 查找答案
        conn.send(answer.encode())
        conn.close()

main()