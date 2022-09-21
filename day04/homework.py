"""
假设有3个文本文件，编写一个程序，将这3个文件合并为
一个大文件 union.txt
"""
# 要合并的三个文件
files = [
    "../day01/1.txt",
    "../day02/2.txt",
    "../day03/3.txt"
]

fw = open("union.txt", 'w')
# 每次取出一个文件复制
for file in files:
    fr = open(file,'r')
    # 边读边写
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
fw.close()

