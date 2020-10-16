class Tool(object):
    count = 0   #定义类属性

    #定义类方法
    @classmethod
    def Tool_def(cls):
        print(cls.count)   #调用类属性
    #初始化
    def __init__(self,name):
        self.name = name
        Tool.count += 1

dada = Tool("dada")
xixi = Tool("xixi")
Tool.Tool_def()
