"""
文件写操作演示
打开文件后，每次写操作都是从上次的位置继续往后
写操作不会自动添加格式，所有各自都自己控制
"""
#写方式打开
# fw = open("file.txt",'w') # 文本方式
# fw = open("file.txt",'wb') # 二进制
fw = open("file.txt",'ab') # 追加

# 写入内容
n = fw.write("大吉大利\n".encode())
print(n)
n = fw.write("今晚吃鸡\n".encode())
print(n)

# 将列表中的每一项分别写入
# data = ["张三 ","李四 ","王五 ","赵柳 "]
# fw.writelines(data)

# 关闭
fw.close()


