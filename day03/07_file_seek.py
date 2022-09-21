"""
文件读写偏移量
"""
#　可读可写
file = open("file.txt","wb+")

file.write(b"Hello world")
file.flush()

print("偏移量：",file.tell()) # 11

#　设置文件偏移量的位置
# file.seek(5,0) #　开头为起点向后移动５字节
file.seek(-5,2) #　结尾为起点向前移动５字节　二进制方式打开

# data = file.read()
# print("读取:",data)

file.write(b"AAA")

file.close()