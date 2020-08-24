gl_list = ["ww","aa","kpkpkp"]


def menu(temp_list):
    """+=在列表中的实际"""
    temp_list.append("ccccccc")
    print(temp_list)
    temp_list += ["popo"]
    print(temp_list)
    print("continue")

print(gl_list)
menu(gl_list)
