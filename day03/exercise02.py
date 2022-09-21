"""
重点练习 ！！
2. 编写一个函数 copy,参数传入一个文件（可以带路径），执行函数
将这个文件复制到当前程序运行的目录下

文件复制本质 ：  从一个文件中读取数据，将其原样的写入到另一个文件

def copy(filename):
    pass

copy("/home/tarema/下载/abc.py")
"""

def copy(filename):
    fr = open(filename,'rb')
    new_file = filename.split('/')[-1] # 提取文件名
    fw = open(new_file, 'wb')
    # 循环边读边写
    while True:
        data = fr.read(1024)
        if not data:
            break # 如果data为空字串 则结束循环
        fw.write(data)
    fr.close()
    fw.close()


copy("/home/tarena/下载/ke.jpeg")