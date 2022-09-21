"""
os 模块下的文件处理函数
"""
import os

# 获取文件大小
size = os.path.getsize("union.txt")
print("文件大小(字节):",size)

# 获取一个文件夹中的内容
files = os.listdir(".")
print(files)

# 判断文件是否存在
res = os.path.exists("union1.txt")
print(res)