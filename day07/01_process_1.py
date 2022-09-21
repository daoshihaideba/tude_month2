"""
进程基础示例1
"""
import multiprocessing as mp
from time import sleep

a = 1 # 定义变量

# 进程函数
def func():
    print("开始执行一个任务....")
    sleep(3) # 模拟做事的时间
    print("任务终于完成喽...")
    global a
    print("a =",a)
    a = 10000 # 修改全局变量

# 实例化进程对象
process = mp.Process(target=func)
process.start() # 启动进程 --》 自动执行绑定函数

print("我也执行一个任务....")
sleep(4) # 模拟做事的时间
print("哈哈我也完成喽...")

process.join() # 如果结束阻塞一定表示子进程已经执行完了
print("a :",a) # 1
