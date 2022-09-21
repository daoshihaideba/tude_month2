"""
练习1： 求100000以内质数之和
质数 ： 只能被1和其本身整除的 > 1的整数
分别使用一个进程和4个进程完成这件事情，统计执行时间
* 一个进程做这件事用时
* 4个进程将100000分为4等份，每个进程分别求 其中一份的质数之和
  再将4个结果加在一起，4个进程同时进程 求最终总共时间
提示： import time    time.time()

* 多进程无阻塞的任务在执行时，时间效率也会有提升
* 并不是进程越多越好，和cpu内核数量也有关系
"""
import time
from multiprocessing import Process ,Queue

# 判断一个数是否为质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            return False
    return True

# def process_1():
#     prime = [] # 存放质数
#     for i in range(1,100001):
#         if is_prime(i):
#             prime.append(i)
#     print(sum(prime))
#
# begin = time.time()
# process_1() # 时间: 13.482529401779175
# print("时间:",time.time() - begin)

#######################4个进程#########################

q = Queue()
# 定义一个进程类，用作求 从  begin--end 之间所有质数之和
class Prime(Process):
    def __init__(self,begin,end):
        self.begin = begin
        self.end = end
        super().__init__()

    def run(self):
        prime = []  # 存放质数
        for i in range(self.begin,self.end):
            if is_prime(i):
                prime.append(i)
        q.put(sum(prime))

def process_10():
    # 4次循环
    for i in range(1,100001,10000):
        p = Prime(i,i+10000)
        p.start()
    res = 0
    for i in range(10):
        res += q.get()
    print(res)

begin = time.time()
process_10() # 时间: 7.947280168533325
print("时间:",time.time() - begin)

# 时间: 13.482529401779175