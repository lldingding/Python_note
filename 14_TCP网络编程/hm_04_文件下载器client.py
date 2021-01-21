"""
1.导入模块
2.创建套接字
3.建立连接
4.接收用户输入的文件名
5.发送文件名到服务端
6.创建新文件，等待接收数据保存
7.接收服务端发送的数据，保存至本地（循环）
8.关闭套接字
"""
#1.导入模块
import socket
#2.创建套接字
tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#3.建立连接
tcp_client_socket.connect(("192.168.110.128",8090))
#4.接收用户输入的文件名
file_name = input("请输入要下载的文件名：")
#5.发送文件名到服务端
tcp_client_socket.send(file_name.encode())
#6.创建新文件，等待接收数据保存
with open("/home/ubuntu/桌面/"+file_name , "w") as file:
    while True:
        recv_data = tcp_client_socket.recv(1024).decode()
        if recv_data:
            #7.接收服务端发送的数据，保存至本地（循环）
            file.write(recv_data)
        else:
            break
#8.关闭套接字
tcp_client_socket.close()


