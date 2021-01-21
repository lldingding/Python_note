#导入模块
import socket
#创建套接字socket
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定ip和端口，“”代表本主机所有ip
udp_socket.bind(("",8888))
#接收 udp_socket拆包 数据+ip来源
recv_data,ip_port = udp_socket.recvfrom(1024)
#打印+解码
print(recv_data.decode("gbk"))

#关闭套接字socket
udp_socket.close()