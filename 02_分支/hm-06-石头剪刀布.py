# 玩家出拳/ 石头（1）剪刀（2）布（3）
player = int(input("请出拳，，出招==="))
# 电脑出拳 石头（1）
rober = 1
# 比较规则
# 玩家赢
if ((player == 1 and rober == 2)
        or (player == 2 and rober == 3)
        or (player == 3 and rober == 1)):
    print("I WIN happy!!!")
# 玩家平局
elif player == rober:
    print("next ....")
# 玩家输
else:
    print("I am so sad")