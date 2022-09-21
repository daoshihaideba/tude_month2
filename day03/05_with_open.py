"""
with 语句
"""
# with打开文件 生成临时的  文件对象   fr = open("file.txt")
with open("file.txt") as fr:
    data = fr.read()
    print(data)
#语句块结束ｆｒ就不能用了，也无需ｃｌｏｓｅ