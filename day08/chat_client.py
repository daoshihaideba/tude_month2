"""
聊天室客户端
"""
from socket import *
from multiprocessing import Process

# 访问服务器的地址
ADDR = ("121.5.90.43", 8888)


# 进入聊天室
def do_login(sock):
    while True:
        name = input("请输入昵称：")
        if ' ' in name or len(name) < 3 or len(name) > 12:
            print("昵称需3-12个字符且不能有空格")
            continue # 名字不合格重新给那些输入
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), ADDR)
        res, addr = sock.recvfrom(128)  # 接收结果
        if res == b'OK':
            print("您已进入聊天室")
            return name
        else:
            print("该昵称已存在")


# 聊天
def do_chat(sock, name):
    # 创建子进程，且父进程退出时子进程随之退出
    p = Process(target=recv_msg, args=(sock,), daemon=True)
    p.start()
    send_msg(sock, name)


# 进入聊天室后所有的接收都在这
def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print("\n"+data.decode()+"\n发言：",end='')


# 发送消息
def send_msg(sock, name):
    while True:
        content = input("发言：")
        if not content or content == '##':
            break
        msg = "CHAT %s %s" % (name, content)
        sock.sendto(msg.encode(), ADDR)


# 退出聊天室
def do_quit(sock, name):
    msg = "QUIT " + name
    sock.sendto(msg.encode(), ADDR)
    print("您已退出聊天室")


# 搭建网络
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    name = do_login(sock)  # 进入聊天室
    try:
        do_chat(sock, name)  # 聊天
    except:
        # 捕获异常后什么都不做只是继续执行代码，
        # 防止客户端异常退出造成用户名无法后续使用
        pass
    do_quit(sock, name)  # 退出聊天室
    sock.close()


if __name__ == '__main__':
    main()
