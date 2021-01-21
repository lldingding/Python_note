#导入模块
import socket
#创建套接字socket
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_socket.sendto("niaho".encode(),("192.168.110.1",8082))

#关闭套接字socket
udp_socket.close()