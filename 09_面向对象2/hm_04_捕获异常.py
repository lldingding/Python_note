try:
    a = int(input("请输入: "))

    b = 8 / a

    print(b)
except ValueError:
    print("输入错误类型")
except Exception as result:
    print("未知错误 %s" % result)