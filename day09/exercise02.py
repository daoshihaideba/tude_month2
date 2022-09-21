"""
模拟龟兔赛跑场景，赛程一个100米，创建类，实例化两个对象，
分别表示龟和兔，实例化对象时可以传入龟和兔的速度,
龟每秒1米（忍者神龟），
兔每秒5米，但是兔每跑10米休息2秒，
执行这两个进程，每隔2秒打印一次两者跑的距离，直到两者都跑到终点为止。
"""
from threading import Thread
from time import sleep

# 运动员类
class Athlete(Thread):
    total = 100 # 赛程
    def __init__(self,player,speed):
        self.player = player
        self.speed = speed # 没秒速度
        self.distance = 0 # 运动员跑的距离
        super().__init__()

    def run(self):
        pass

# 龟类运动员
class Turtle(Athlete):
    def run(self):
        while self.distance < Turtle.total:
            sleep(1)
            self.distance += self.speed

# 兔子类运动员
class Rabbit(Athlete):
    def run(self):
        while self.distance < Turtle.total:
            sleep(1)
            self.distance += self.speed
            if self.distance % 10 == 0:
                sleep(2)

# 运动员对象
t = Turtle("龟跑跑",1)
r = Rabbit("兔懒懒",5)
t.start()
r.start()

while t.distance < 100 or r.distance < 100:
    sleep(2)
    print("%s 跑了 %d 米"%(t.player,t.distance))
    print("%s 跑了 %d 米"%(r.player,r.distance))
