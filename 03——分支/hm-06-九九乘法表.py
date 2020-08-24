#生成九九乘法表
#父循环
i = 1
while i <= 9:
    #子循环
    j = 1
    while j <= i:
        print("%d * %d = %d" % (j,i,i * j),end="\t")
        j += 1
    print(" ")
    i += 1

