# 生成
# *
# **
# ***
# ****
# 父循环
i = 1   #计数初数
while i <= 4:
    #子循环
    j = 1   #计数初数
    while j <= i:
        print("*",end="")
        j += 1
    print("")
    i += 1