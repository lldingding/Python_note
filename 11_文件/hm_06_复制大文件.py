#打开文件
file_old = open("README.py")
file_new = open("README3.0.py","w")
#读写文件
while True:
    test = file_old.readline()
    if test is None:
        break
    file_new.write(test)
#关闭文件
file_new.close()
file_old.close()