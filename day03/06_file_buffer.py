"""
文件缓存区
"""
# 设置行缓冲  换行刷新
# fw = open("file.txt",'w',buffering=1)

#　设置缓冲大小
fw = open("file.txt",'wb',buffering=10)

while True:
    msg = input("请输入:")
    if not msg:
        break
    fw.write(msg.encode())
    # fw.flush() #　刷新缓冲   ctrl-s

fw.close()