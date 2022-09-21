"""
一个父进程创建多个子进程
* 所有子进程都拷贝父进程内存空间
* 每个子进执行不同的函数
"""
from multiprocessing import Process
import os,sys
from time import sleep

# def th1():
#     # sys.exit("一号子进程挂了")
#     sleep(4)
#     print("吃饭")
#     print(os.getppid(), "--", os.getpid())
#
# def th2():
#     sleep(2)
#     print("睡觉")
#     print(os.getppid(), "--", os.getpid())
#
# def th3():
#     sleep(3)
#     print("打豆豆")
#     print(os.getppid(), "--", os.getpid())

# p1 = Process(target=th1)
# p1.start()
# p2 = Process(target=th2)
# p2.start()
# p3 = Process(target=th3)
# p3.start()

# # 循环创建子进程
# jobs = [] # 存储进程对象
# for th in [th1,th2,th3]:
#     p = Process(target=th)
#     jobs.append(p) # 添加进程对象
#     p.start()
#
# # 等待所有子进程都结束
# for i in jobs:
#     i.join()
#
# print("所有子进程执行完毕")

##################一个进程函数实现方案##################

def th(sec,info):
    sleep(sec)
    print(info)
    print(os.getppid(), "--", os.getpid())

# 循环创建子进程
jobs = [] # 存储进程对象
for arg in [(4,"吃饭"),(2,"睡觉"),(3,"打豆豆")]:
    p = Process(target=th,args=arg)
    jobs.append(p) # 添加进程对象
    p.start()

# 等待所有子进程都结束
for i in jobs:
    i.join()

print("所有子进程执行完毕")



