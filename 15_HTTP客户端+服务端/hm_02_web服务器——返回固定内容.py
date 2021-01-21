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


def request_handler(new_client_socket):
    # recv_data = new_client_socket.recv(1024).decode()
    recv_data = new_client_socket.recv(1024)
    # print(recv_data)
    if not recv_data:
        print("客户端下线了！！！！！")
        new_client_socket.close()
        return
    else:
        # 1.响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 2.响应头
        response_handler = "Server: PythonKK/3.9\r\n"
        # 3.响应空行
        response_blanks = "\r\n"
        # 4.响应主体
        response_body = "<html><h>HelloWorld+++++++++++++!<h/><html/>"
        # 5.拼接
        response_data = response_line + response_handler + response_blanks + response_body
        new_client_socket.send(response_data.encode())
        new_client_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 3.设置地址重用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    tcp_server_socket.bind(("",8080))
    tcp_server_socket.listen(128)
    while True:
        """循环接收连接"""
        new_client_socket,ip_port = tcp_server_socket.accept()
        print("come on!!! [%s]" % str(ip_port))
        request_handler(new_client_socket)

    # 11.关闭连接
    # tcp_server_socket.close()


if __name__ == "__main__":
    main()

