"""
线程基础示例2
带有参数的线程函数
"""
from threading import Thread
from time import sleep

# 带有参数的线程函数
def func(sec,name):
    print("%s 开始执行..."%name)
    sleep(sec)
    print("%s 线程执行完毕..."%name)

# 循环创建线程
# jobs = []
for i in range(5):
    t = Thread(target=func,
               args=(2,),
               kwargs={"name":"T-%d"%i},
               daemon=True # 分支线程随主线程结束
               )
    # jobs.append(t) # 存储线程对象
    t.start()

# for i in jobs:
#     i.join()
# print("所有线程结束")