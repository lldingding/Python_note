"""
一、功能
1、发送信息
2、接收信息
3、退出系统

二、框架的设计
1、发送信息 send_msg()
2、接收信息 recv_msg()
3、程序的主入口 main()
4、当程序独立运行的时候，才启动聊天器

三、实现步骤
1、发送信息 send_msg()
1) 定义变量接收用户与输入的接收方的IP地址
2）定义变量接收用户与输入的接收方的端口号
3)定义变量接收用户与输入的接收方的内容
4）使用socket的sendto() 发送信息

2、接收信息 recv_msg()
1) 使用socket 接收数据
2）解码数据
3）输出显示

3、主入口main()
1）创建套接字
2）绑定端口
3）打印菜单（循环）
4）接收用户输入的选项
5）判断用户的选择，并且调用对应的函数
6）关闭套接字
"""
import socket


def recv_msg(imput_socket):
    recv_data,ip_port = imput_socket.recvfrom(1024)
    print("接收[%s]来自%s" % (recv_data.decode("gbk"),ip_port))


def send_msg(imput_socket):
    comment = input("请输入信件内容: ")
    ip = input("请输入收件ip: ")
    port = input("请输入收件port: ")
    addr = (ip,port)
    imput_socket.sendto(comment.encode(),addr)


def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",8888))

    while(True):
        print("------------------")
        print("---1.接收----------")
        print("---2.发送----------")
        print("---3.退出----------")
        input_number = input("请选择系统： ")
        if input_number == "1":
            recv_msg(udp_socket)
        elif input_number == "2":
            send_msg(udp_socket)
        elif input_number == "3":
            break
        else:
            print("输入错误，请重新输入")
    udp_socket.close()


if __name__ == "__main__":
    main()