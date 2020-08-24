def a_print(char,num):
    """函数1

    :param char: 字符形式形参
    :param num: 次数
    """
    print(char * num)


def b_print(char,num):
    """调用函数1    次数5次

    :param char: 字符形式形参
    :param num: 次数
    """
    i = 1
    while i < 5:
        a_print(char,num)
        i += 1


b_print("w",4)

