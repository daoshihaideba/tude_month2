"""
编写一组程序，在实现如下功能 用户输入单词，会得到单词解释
在客户端输入单词，单词会发送到服务端进行查询，如果查询到了
则把解释回复给客户端让客户端显示，如果没有查询到则给客户端回复
"Not Found"
收单词  -》 查单词解释  -》 发送解释 （Not Found）
"""
from socket import *

# 查询单词函数
def query_word(word):
    fr = open("../day16/dict.txt", 'r')
    # 迭代每次取一行
    for line in fr:
        tmp = line.split(' ',1) # 将一行内容按照空格切割1次
        if tmp[0] > word:
            break # 遍历到的单词已经大于word就肯定找不到了
        elif tmp[0] == word:
            return tmp[1].strip() # 取出字符串两侧空格
    return "Not Found!"

def main():
    # 创建udp套接字
    udp_socket=socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 8888))
    # 循环先收后发
    while True:
        word,addr = udp_socket.recvfrom(1024)
        # 查询单词解释
        mean = query_word(word.decode())
        udp_socket.sendto(mean.encode(),addr)
    udp_socket.close()

main() # 启动