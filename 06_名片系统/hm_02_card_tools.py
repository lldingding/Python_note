card_list = []

def gn_menu():
    print("++++++++++++++++++")
    print("情况【1】 新增名片")
    print("情况【2】 显示名片")
    print("情况【3】 查询名片")
    print("------------------")
    print("情况【0】 退出系统")
    print("++++++++++++++++++")

def qk_xz():

    name_in = input("请输入新增用户姓名= ")
    phone_in = input("请输入新增用户手机= ")
    qq_in = input("请输入新增用户qq= ")
    email_in = input("请输入新增用户邮箱= ")
    list_dict = {"name": name_in,
                 "phone": phone_in,
                 "qq": qq_in,
                 "email": email_in}
    card_list.append(list_dict)
    print("成功新增一个用户")
    print(card_list)

def qk_xs():
    if card_list != 0:
        print("姓名\t\t\t手机\t\t\t\tqq\t\t\t\t邮箱")
        for card_dict in card_list:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
    else:
        print("数据库内无数据")

def qk_cx():
    recive_name = input("请输入姓名= ")
    global card_list
    for card_dict in card_list:
        if card_dict["name"] == recive_name:
            print("查询信息成功")
            print("姓名\t\t\t手机\t\t\t\tqq\t\t\t\t邮箱")
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))

            action = input("选择修改用户【1】删除用户【2】返回【0】= ")
            if action == "1":
                card_dict = xiugai(card_dict, card_list)
                print("姓名\t\t\t手机\t\t\t\tqq\t\t\t\t邮箱")
                print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))
            elif action == "2":
                card_list.remove(card_dict)
                print("成功删除用户")
            else:
                print("已退出模式3")
            break
    else:
        print("查无此人")

def xiugai(dict,list_new):
    list_new.remove(dict)
    a = input("请输入新姓名，保持则直接enter= ")
    if len(a) > 0:
        dict["name"] = a
    b = input("请输入新手机，保持则直接enter= ")
    if len(b) > 0:
        dict["phone"] = b
    c = input("请输入新qq，保持则直接enter= ")
    if len(c) > 0:
        dict["qq"] = c
    d = input("请输入新邮箱，保持则直接enter= ")
    if len(d) > 0:
        dict["email"] = d
    list_new.append(dict)
    return  dict

