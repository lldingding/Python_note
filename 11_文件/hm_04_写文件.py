#默认只有r权限，w权限代表只写，覆盖写
file_write = open("README.py","w")
#写
file_write.write("django")
#关闭文件
file_write.close()