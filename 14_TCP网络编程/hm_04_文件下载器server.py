"""
1.导入模块
2.创建套接字
3.绑定端口
4.设置监听，套接字由主动变成被动
5.接收客户端连接
6.接收客户端发送的文件名
7.根据文件名读取文件内容
8.把读取内容发送给客户端
9.关闭和客户端的连接
10.关闭服务器
"""
#1.导入模块
import socket
#2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#3.绑定端口
tcp_server_socket.bind(("",8090))
#4.设置监听，套接字由主动变成被动
tcp_server_socket.listen(128)
while True:
    #5.接收客户端连接
    new_socket,ip_port = tcp_server_socket.accept()
    print("新的客户端【%s】来了" % str(ip_port))
    #6.接收客户端发送的文件名
    recv_file_name = new_socket.recv(1024).decode()
    print("客户端索取的文件名【%s】" % recv_file_name)
    try:
        #7.根据文件名读取文件内容
        with open("/home/ubuntu/PycharmProjects/14_TCP网络编程/"+recv_file_name , "rb") as file:
            while True:
                file_data = file.read(1024)
                if file_data:
                    #8.把读取内容发送给客户端
                    new_socket.send(file_data)
                else:
                    break
    except Exception as result:
        print("文件无法提供下载")
    else:
        print("文件成功下载")
    #9.关闭和客户端的连接
    new_socket.close()
#10.关闭服务器
 #tcp_server_socket.close()
