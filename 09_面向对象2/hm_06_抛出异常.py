def demo(a):
    if a == 1:
        print("11111")
    #抛出异常
    ex  = Exception("米码输入错误")
    raise ex
#捕获异常
try:
    demo(2)
except Exception as result:
    print(result)