# 1.导入模块
# 2.创建套接字
# 3.建立连接
# 4.拼接请求协议
# 5.发送请求协议
# 6.接收服务器响应内容
# 7.保存内容
# 8.关闭连接

import socket
tcp_cilent_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_cilent_socket.connect(("www.baidu.com",80))
# 1.请求行
request_line = "GET / HTTP/1.1\r\n"
# 2.请求头
request_header = "Host:www.baidu.com\r\n"
# 3.请求空行
request_blanks = "\r\n"
# 4.拼接
request_data = request_line + request_header + request_blanks
tcp_cilent_socket.send(request_data.encode())
recv_data = tcp_cilent_socket.recv(4096).decode()
print(recv_data)
loc = recv_data.find("\r\n\r\n")
html_data = recv_data[loc+4:]
print(html_data)
with open("./test.html","w") as file:
    file.write(html_data)
tcp_cilent_socket.close()