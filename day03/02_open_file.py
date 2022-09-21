"""
文件打开示例
"""
# 读方式打开
# file = open("../day02/2.txt",'r')
# print(file)

# 写方式打开  文件不存在创建  存在清空
# file = open("file.txt",'w')
# print(file)

# 写方式打开  文件不存在创建  存在继续往下写
file = open("/home/tarena/month02/day03/file.txt",'a')
print(file)

# 读写操作

# 关闭文件对象
file.close()
