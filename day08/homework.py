"""
练习2：
编写一个程序，用来复制一个文件夹(自选文件夹，文件夹中有若干个
普通文件，没有子目录)，要求为了提高复制的速度，每个文件的复制
都采用一个独立的进程来完成
使用类去完成
"""
from multiprocessing import Process
import os

class CopyFile(Process):
    def __init__(self,dir1,dir2,filename):
        self.dir1 = dir1
        self.dir2 = dir2
        self.filename = filename
        super().__init__()

    def run(self):
        fr = open(self.dir1 + "/" + self.filename,'rb')
        fw = open(self.dir2 + "/" + self.filename,'wb')
        while True:
            data = fr.read(1024)
            if not data:
                break
            fw.write(data)
        fr.close()
        fw.close()

class CopyDir:
    def __init__(self,dir):
        self.old_dir = dir # 要复制的文件夹
        self.new_dir = self._new_dir()

    def _new_dir(self):
        new_dir = self.old_dir.split("/")[-1]
        os.mkdir(new_dir) # 创建文件夹
        return new_dir

    def main(self):
        # 循环取出不同的文件名 给到进程函数
        for file in os.listdir(self.old_dir):
            p = CopyFile(self.old_dir,self.new_dir,file)
            p.start()

copy = CopyDir("/home/tarena/FTP")
copy.main()
