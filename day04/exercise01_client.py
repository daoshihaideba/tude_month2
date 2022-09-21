"""
输入单词  发送单词  接受解释  打印解释
"""
from socket import *

# 访问服务器需要使用的地址
ADDR = ("127.0.0.1",8888)

# 与服务器端交互
def request(udp_socket,word):
    udp_socket.sendto(word.encode(), ADDR)
    mean, addr = udp_socket.recvfrom(1024)
    return mean.decode()


def main():
    # 创建套接字
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    # 循环发送后接收
    while True:
        word = input("要查询的单词：")
        if not word:
            break
        mean = request(udp_socket,word)
        print("%s : %s\n"%(word,mean))
    udp_socket.close()


main()