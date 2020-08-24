class Gun:
    def __init__(self,name):
        self.name = name
        self.num = 0
    def add_num(self,num_list):
        self.num += num_list
        print("%s成功加入子弹%d枚" % (self.name,self.num))
    def shoot(self):
        if self.num == 0:
            print("没有子弹")
            return
        self.num -= 1
        print("%s成功射击 剩余子弹数%d" % (self.name,self.num))

class Solider:
    def __init__(self,solider_name):
        self.solider_name = solider_name
        self.solider_gun = None
    def fire(self):
        """人扳机准备射击"""
        if self.solider_gun is None:
            print("没有枪，不能射击")
            return
        #自动装弹
        self.solider_gun.add_num(50)
        self.solider_gun.shoot()


ak47 = Gun("ak47")
ak47.add_num(10)
ak47.shoot()


baoq = Solider("baoq")
#直接在外面给属性赋值，ak47是对象。对象作属性
baoq.solider_gun = ak47
baoq.fire()
