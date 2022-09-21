"""
练习1 ： 模拟售票过程
假设有500张票，记为  T1 -- T500 放在列表中
有10个窗口 记为 W1 -- W10 ，现在使用10个线程模拟
这10个窗口同时卖票，假设供不应求 ，知道卖完为止。
每卖出一张票 打印  “W1 ---- T250”,每张票出票时间0.1秒
所有票都卖完后打印一句 “票已售罄”
"""
from threading import Thread
from time import sleep

# 生成500张票
tickets = ["T%d"%x for x in range(1,501)]

# 卖票函数
def sell(window):
    while tickets:
        try:
            sleep(0.1)
            print("%s --- %s"%(window,tickets.pop(0)))
        except:
            break

jobs = []
for i in range(1,11):
    t = Thread(target=sell,args= ("W%d"%i,))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
print("票已售罄")
