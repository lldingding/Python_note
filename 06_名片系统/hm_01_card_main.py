#! /usr/bin/python3
import hm_02_card_tools

while True:
    #  此处为功能菜单显示
    hm_02_card_tools.gn_menu()

    num = input("请输入= ")
    print("输入值为=%s" % num)
    if num in ["1", "2", "3"]:
        print("有情况123")
        if num == "1":
            print("情况1 新增名片")
            hm_02_card_tools.qk_xz()
        elif num == "2":
            print("情况2 显示名片")
            hm_02_card_tools.qk_xs()
        else:
            print("情况3 查询名片")
            hm_02_card_tools.qk_cx()
    elif num == "0":
        print("欢迎下次使用本系统")
        break
    else:
        print("请重新输入")