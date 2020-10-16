#打开文件
file_old = open("README.py")
file_new = open("README2.0.py","w")
#读写文件
test = file_old.read()
file_new.write(test)
#关闭文件
file_old.close()
file_new.close()