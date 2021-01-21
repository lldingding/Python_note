# 1.导入模块
# 2.创建套接字
# 3.设置地址重用
# 4.绑定端口
# 5.设置监听
# 6.接收客户端连接
# 7.接收客户端的请求协议
# 8.判断协议是否为空
# 9.拼接响应报文
# 10.发送响应报文
# 11.关闭连接

import socket
from application import app2


class WebServer(object):
    def __init__(self):

        tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 3.设置地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

        tcp_server_socket.bind(("",8000))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket
    def start(self):
        while True:
            """循环接收连接"""
            new_client_socket,ip_port = self.tcp_server_socket.accept()
            print("come on!!! [%s]" % str(ip_port))
            self.request_handler(new_client_socket)

    def request_handler(self,new_client_socket):
        """处理请求函数"""
        # 把请求协议解码，得到请求报文的字符串
        request_data = new_client_socket.recv(1024).decode()
        # print(recv_data)
        if not request_data:
            print("客户端下线了！！！！！")
            new_client_socket.close()
            return
        else:
            response_data = app2.application("./myblog",request_data)
            # loc = request_data.find("\r\n")
            # request_line = request_data[:loc]
            # request_line_list = request_line.split(" ")
            # file_path = request_line_list[1]
            # print("用户连接成功，正在请求【%s】" % "/myblog"+file_path)
            # # 1.响应行
            # response_line = "HTTP/1.1 200 OK\r\n"
            # # 2.响应头
            # response_handler = "Server: PythonKK/3.9\r\n"
            # # 3.响应空行
            # response_blanks = "\r\n"
            # if file_path == "/":
            #     file_path = "/index.html"
            # # 4.响应主体
            # # (2)改进
            # try:
            #     # with open("myblog/index.html" , "rb") as file:
            #     with open("./myblog" + file_path, "rb") as file:
            #         response_body = file.read()
            # except Exception as result:
            #     response_line = "HTTP/1.1 404 Not Found"
            #     response_body = str(result).encode()
            # # 5.拼接
            # response_data = (response_line + response_handler + response_blanks).encode() + response_body
            new_client_socket.send(response_data)
            new_client_socket.close()
    # 11.关闭连接
    # tcp_server_socket.close()


def main():
    wc = WebServer()
    wc.start()


if __name__ == "__main__":
    main()

