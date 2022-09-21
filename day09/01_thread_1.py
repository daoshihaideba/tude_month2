"""
线程基础示例1
"""
from threading import Thread
from time import sleep
import os

a = 1

# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放：黄河大合唱")
    global a
    print("a =",a)
    a = 10000 # 修改全局变量

# 实例化线程对象
t = Thread(target=music)
t.start() # 启动线程执行线程函数

for i in range(4):
    sleep(1)
    print(os.getpid(),"播放：葫芦娃")

t.join() # 阻塞等待分支线程结束
print("a:",a) # 10000
