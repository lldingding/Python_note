#导入模块
import socket
#创建套接字socket
udp_socket = socket.socket(socket.SOCK_DGRAM,socket.AF_INET)
#关闭套接字socket
udp_socket.close()