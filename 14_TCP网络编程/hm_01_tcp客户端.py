import socket
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
addr = ("192.168.110.1",8080)
tcp_socket.connect(addr)

tcp_socket.send("leo.hello,groat".encode())
tcp_socket.close()