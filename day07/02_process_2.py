"""
进程基础示例 2
"""
from multiprocessing import Process
from time import sleep

# 带有形参的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

# 实例化进程对象 按照位置传参
# p = Process(target=worker,args=(2,"Tom"))

# 按照关键字传参
p = Process(target=worker,
            args=(2,),
            kwargs = {"name":"Tom"},
            daemon=True) # 该子进程会随着父进程而退出
p.start() # 启动进程

sleep(4)
