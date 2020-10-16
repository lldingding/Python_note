#打开文件，返回对象file接收
file = open("README.py")
#读文件
test = file.read()
print(test)
print("--------")
#每次read时，文件指针会到末尾
test = file.read()
print(test)
#关闭文件
file.close()