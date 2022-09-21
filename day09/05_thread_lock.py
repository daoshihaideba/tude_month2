"""
同步互斥方法 之  Lock
"""
from threading import Thread,Lock

a = b = 0  # 共享资源
lock = Lock() # 锁对象

def value():
    while True:
        lock.acquire() # 上锁
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release() # 解锁

t = Thread(target=value)
t.start()

while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()