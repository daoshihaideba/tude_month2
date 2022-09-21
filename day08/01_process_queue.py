"""
进程间通信之消息队列
"""
from multiprocessing import Process, Queue
import sys

q = Queue()  # 消息队列  父进程创建子进程直接用

# 子进程
def handle(x, y):
    while True:
        cmd = q.get()  # 从消息队列获取指令
        if cmd == "+":
            print("\n%d + %d = %d" % (x, y, x + y))
        elif cmd == '-':
            print("\n%d - %d = %d" % (x, y, x - y))
        else:
            sys.exit("子进程错误") # 子进程结束

p = Process(target=handle,args=(6,4))
p.start()

while True:
    cmd = input("运算符:")
    q.put(cmd) # 存入消息队列
