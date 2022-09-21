"""
自定义进程类
"""
from multiprocessing import Process
from time import sleep

# 进程类 ： 既可以创建进程  又可以把进程要做的事情放在类中
class MyProcess(Process):
    def __init__(self,mv,n):
        self.mv = mv
        self.n = n
        super().__init__() # 加载父类实例变量

    def run(self):
        """干点啥自己写"""
        for i in range(self.n):
            sleep(2)
            print("播放：",self.mv)

player = MyProcess("西虹市首富",3)
player.start() # 创建进程 自动运行 run


########### Process 猜想 #################
# class Process:
#     def __init__(self,target=None):
#         self.target = target
#
#     def run(self):
#         self.target()
#
#     def start(self):
#         """...进程创建"""
#         self.run()



