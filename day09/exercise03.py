"""
创建2个分支线程，一个分支线程打印1--52这52个数字
一个分支线程打印A--Z这26个字母，两个分支线程一起执行
打印顺序为 12A34B....5152Z
"""
from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i + 1)
        lock2.release()

def print_chr():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t1 = Thread(target=print_num)
t2 = Thread(target=print_chr)

lock2.acquire() # 先给lock2上锁

t1.start()
t2.start()