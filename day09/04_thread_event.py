"""
线程同步互斥方法之 Event
"""
from threading import Thread,Event

msg = None # 通信变量
e1 = Event() # event 对象  e.wait()  e.set()  e.clear()
e2 = Event()

# 分支线程函数
def 杨子荣():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e1.set() # 解除后面的wait阻塞
    e2.wait()
    print("开始地下工作...")

t = Thread(target=杨子荣)
t.start()

print("说对口令才是自己人")
e1.wait() # 等待一下  13行执行完
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
    e2.set()
else:
    print("打死他...无情啊雕哥...")
