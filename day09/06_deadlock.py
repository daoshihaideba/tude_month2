"""
死锁现象
"""
from threading import Thread,Lock
from time import sleep

# 账户
class Account:
    def __init__(self,id,balace,lock):
        self.id = id
        self.balance = balace
        self.lock = lock

    def get(self,amount):
        self.balance -= amount

    def put(self,amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

tom = Account('tom',10000,Lock())
abby = Account('abby',2000,Lock())

# 转账
def transfer(from_,to,amount):
    from_.lock.acquire() # from上锁
    from_.get(amount) # 钱减少
    from_.lock.release() # 这里不会产生死锁

    sleep(0.1) # 网路延迟
    to.lock.acquire() # to上锁
    to.put(amount)
    # from_.lock.release() # 这里会产生死锁
    to.lock.release()

# transfer(tom,abby,3000)

# 相互转账
t1 = Thread(target=transfer,args=(tom,abby,2000))
t2 = Thread(target=transfer,args=(abby,tom,2000))
t1.start()
t2.start()
t1.join()
t2.join()

print("Tom:",tom.getBalance())
print("Abby:",abby.getBalance())

