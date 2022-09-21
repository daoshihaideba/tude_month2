"""
练习 1 ： 完成大文件拆分
将一个大文件拆分两个较小的文件，要求拆分的过程使用两个子进程同时执行，
以提高拆分速度。
文件拆分按照字节大小划分为上下两个部分
在拆分完成后打印一句 “拆分完毕”

提示 ： os.path.getsize()
"""
from multiprocessing import Process
import os

# 要拆分的文件
filename = "/home/tarena/下载/zhao.jpeg"
# 测文件大小
size = os.path.getsize(filename)

# 拷贝文件上半部分
def top():
    fr = open(filename,'rb')
    fw = open("top.jpeg",'wb')
    n = size // 2
    while n >= 1024:
        data = fr.read(1024)
        fw.write(data)
        n -= 1024
    fw.write(fr.read(n))
    fr.close()
    fw.close()

# 拷贝文件下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open("bot.jpeg", 'wb')
    fr.seek(size // 2,0) # 文件偏移量到中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

jobs = [] # 存储进程对象
for th in [top,bot]:
    p = Process(target=th)
    jobs.append(p) # 添加进程对象
    p.start()

# 等待所有子进程都结束
for i in jobs:
    i.join()

print("拆分完毕")





