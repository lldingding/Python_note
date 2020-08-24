# 定义列表
name_list = ["zhangsan","lisi","wangwu","daodao"]
# 修改列表
name_list[3] = "ee"
#取索引
a = name_list.index("lisi")
# 列表增加
name_list.append("gigi")
name_list.insert(1,"xixi")
list = ["dingding"]
name_list.extend(list)
# 删除列表
del name_list[1]
name_list.remove("dingding")
name_list.pop(1)
#name_list.clear()
# 统计
d = len(name_list)
# 排序
name_list.sort()
name_list.sort(reverse=True)
name_list.reverse()
# 打印列表
print(name_list)
print(name_list[3])
print(d)
print(a)