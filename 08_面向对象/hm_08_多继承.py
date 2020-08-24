class Xiaogou(object):
    def eat(self):
        print("吃吃吃")

class Dagou(object):
    def play(self):
        print("玩玩万")

class Xtq(Xiaogou,Dagou):
    def pao(self):
        pass

tom = Xtq()
tom.eat()
tom.play()
