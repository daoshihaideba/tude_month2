"""
练习2：
编写一个程序，用来复制一个文件夹(自选文件夹，文件夹中有若干个
普通文件，没有子目录)，要求为了提高复制的速度，每个文件的复制
都采用一个独立的进程来完成

提示 ： os.listdir()
       os.mkdir("dir")
"""
from multiprocessing import Process
import os

dir1 = "/home/tarena/FTP" # 要复制的文件夹
dir2 = "FTP"
os.mkdir(dir2) # 创建文件夹

# 每个进程都是复制文件
def copy(filename):
    fr = open(dir1 + "/" + filename,'rb')
    fw = open(dir2 + "/" + filename,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

# 循环取出不同的文件名 给到进程函数
for file in os.listdir(dir1):
    p = Process(target=copy,args=(file,))
    p.start()


