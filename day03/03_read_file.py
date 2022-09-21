"""
文件读操作示例
打开文件后每次读取都会从上次的位置继续往下读
读取到文件结尾继续往后读则会返回空字串但是不会报错
"""
# 读方式打开文件
# fr = open("file.txt",'r') # 本文打开
fr = open("file.txt",'rb') # 二进制打开

# 读取内容
data = fr.read()
print(data)

# 每次读取一个字符，读取全部内容打印出来，自动结束
# while True:
#     data = fr.read(1)
#     if data == "":
#         break
#     print(data,end="")

# 按行读取内容  每次读取到换行或者指定的字符个数
# line = fr.readline()
# print(line)

# 读取多行内容
# lines = fr.readlines(15)
# print(lines) # 得到列表，列表每一项就是一行内容

# 迭代取值 每次取一行内容
# for line in fr:
#     print(line)


# 关闭文件
fr.close()
