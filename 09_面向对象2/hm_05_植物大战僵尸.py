class NewGame(object):
    #静态属性 历史最高分
    best_goal = 0
    #静态方法（帮助文档）
    @staticmethod
    def help():
        print("欢迎英雄回家！！！")
    #类方法（调用静态属性，查看历史最高分）
    @classmethod
    def history(cls):
        print(cls.best_goal )
    #初始化
    def __init__(self,name):
        play_name = name
    #开始游戏
    def start(self):
        print("start !!!")
        #更改历史最高分
        NewGame.best_goal = 99999
#查看游戏帮助
NewGame.help()
#查看历史最高分
NewGame.history()
#创建对象
xiaoqiang = NewGame("xiaoqiang")
#开始游戏
xiaoqiang.start()
#查看历史最高分
NewGame.history()
