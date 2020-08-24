class Person:
    """人类"""
    #初始值
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    #吃东西
    def eat(self):
        print("%s 吃东西了" % self.name)
        self.weight += 1
    #跑步
    def run(self):
        print("%s 跑步了" % self.name)
        self.weight -= 0.5
    #总结
    def __str__(self):
        return "%s 的体重为 %.2f" % (self.name,self.weight)

tom = Person("tom",90)
tom.eat()
tom.run()
print(tom)