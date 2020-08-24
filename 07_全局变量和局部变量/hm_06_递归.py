# 求1+2+3+......+num的和
def add(num):
    """递归"""
    # 出口
    if num == 1:
        return 1
    # 调用函数add
    temp=add(num-1)
    # 相加
    return num + temp


a = add(3)
print(a)

