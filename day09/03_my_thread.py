"""
自定义线程类
"""
from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self,song):
        self.song = song
        super().__init__()  # 加载父类实例变量
    
    # 重写run
    def run(self):
        for i in range(3):
            sleep(2)
            print("播放:",self.song)

player = MyThread("黑猫警长")
player.start() # 创线程 --》 run


