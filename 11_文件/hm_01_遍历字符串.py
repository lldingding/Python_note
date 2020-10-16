#*-* coding:utf8 *-*
str = u"heloop最高"
for c in str:
    print(c)

#python2.x中加入  “#*-* coding:utf8 *-*”  才能遍历中文，否则中文是乱码
#python2.x编码格式ascii，3.x的uft-8