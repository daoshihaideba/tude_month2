"""
3. 编写一个程序，循环的向一个文件（my.log）中写入如下内容:　
　　1. Thu Mar 24 17:32:44 2022
　　2. Thu Mar 24 17:32:46 2022
　　3. Thu Mar 24 17:32:48 2022
　　4. Thu Mar 24 17:34:09 2022
　　5. Thu Mar 24 17:34:11 2022
   每隔２秒写入一行,每行内容写入后需要实时显示出来　
   当程序结束后,如果重新启动，会继续往下写，并且序号能够衔接
提示：　import time
       time.ctime()  获取当前时间
       time.sleep(2) 暂停执行２秒
"""
import time

# 每行实时显示
log = open("my.log",'a+',buffering=1)

log.seek(0,0) # 文件偏移量到开头

n = len(log.readlines()) + 1 # 序号 = 已有行数 + 1
while True:
    msg = "%d. %s\n"%(n,time.ctime())
    log.write(msg)
    n += 1  # 序号增加
    time.sleep(2)
