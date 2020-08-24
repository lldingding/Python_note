class Dog(object):
    def eat(self):
        print("dddddd")

class Xtq(Dog):
    def eat(self):
        print("gagaga")

class Person(object):
    def paly(self,gou):
        gou.eat()

# gou = Dog()

gou = Xtq()
xiaoming = Person()
xiaoming.paly(gou)
