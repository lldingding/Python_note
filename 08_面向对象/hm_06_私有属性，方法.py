class Dog(object):
    def __init__(self,name):
        """加#为私有"""
        # self__name = name
        self.name = name
    # def __eat(self):
    #     print("wangwangwang")
    def eat(self):
        print("wangwangwang")


wangcai = Dog("wangcai")
print(wangcai.name)
wangcai.eat()

