"""
完成一个简易的http服务程序
"""
from socket import *


# 具体与浏览器交互 给浏览器提供网页
class Handle:
    def __init__(self, html):
        self.html = html  # 网页所在位置 ./static

    # 接受请求-》解析
    def do_http(self, conn):
        request = conn.recv(1024)  # 接收请求
        if not request:
            return  # 防止浏览器主动异常断开
        info = request.decode().split(' ')[1]
        print("请求内容:", info)  # 请求内容
        self.send_response(conn, info)  # 发送响应

    # 发送响应 组织响应-》发送
    def send_response(self, conn, info):
        # info 分情况讨论： 请求的内容是否存在  主页还是其他网页
        if info == '/':
            info = "/index.html"

        try:
            fr = open(self.html + info, 'rb')
        except:
            # 请求的网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "The requested URL %s was not found on this server." % info
            conn.send(response.encode())
        else:
            # 请求的网页存在
            response = b"HTTP/1.1 200 OK\r\n"
            response += b"Content-Type:text/html\r\n"
            response += b"\r\n"
            response += fr.read()
            conn.send(response)


# 搭建网络模型
class HTTPServer:
    def __init__(self, host="", port=0, html=None):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.handle = Handle(html)  # 跨类的调用
        self.sock = self._create_socket()

    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        return sock

    # 循环的tcp网络服务
    def main(self):
        self.sock.listen(3)
        print("Listen the port %s" % self.port)
        # 循环处理浏览器连接
        while True:
            conn, addr = self.sock.accept()
            self.handle.do_http(conn)  # http交互
            conn.close()


if __name__ == '__main__':
    # 实例化对象 -》 对象调用方法启动网络服务
    http = HTTPServer(host="0.0.0.0", port=8888, html="./static")
    http.main()  # 启动网络服务 （准备__init__，核心 main，收尾 close）
