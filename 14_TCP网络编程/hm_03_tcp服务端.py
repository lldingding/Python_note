import socket
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定ip和port
tcp_socket.bind(("",6552))
#listen监听
tcp_socket.listen(128)
#accept等待连接
new_socket,client_ip_port = tcp_socket.accept()
print("【%s】客户端来了" % str(client_ip_port))
#收发
revc_data = new_socket.recv(1024).decode("GBK")
print(revc_data)
#关闭new的套接字
new_socket.close()
#关闭套接字
tcp_socket.close()