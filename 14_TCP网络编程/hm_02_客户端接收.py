import socket
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
addr = ("192.168.110.1",8080)
tcp_socket.connect(addr)
#接收+decode解码
recv_data = tcp_socket.recv(1024).decode("GBK")
print(recv_data)
#关闭套接字
tcp_socket.close()