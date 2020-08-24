xiaoming_dict = {"name": "lidong",
                 "age": 21,
                 "gender": "man",}
#增加和修改
xiaoming_dict["eat"] = "apple"
#删除
xiaoming_dict.pop("gender")
#合并
temp_dict = {"game": "qq"}
xiaoming_dict.update(temp_dict)


print(xiaoming_dict["age"])
print(xiaoming_dict)