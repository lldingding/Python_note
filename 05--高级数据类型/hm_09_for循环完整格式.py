name_list = [{"name": "tutu"},
             {"name": "lili"},
             {"name": "keke"}
]
find_name = "keke"

for a_name in name_list:
    if a_name["name"] == find_name:
       print("找到")
       break
else:
    print("没找到")

print("above all")