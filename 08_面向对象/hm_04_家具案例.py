class HomeList:
    def __init__(self,list_name,list_area):
        self.list_name = list_name
        self.list_area = list_area
    def __str__(self):
        return "%s --- %s" % (self.list_name,self.list_area)


class House:
    def __init__(self,name,area):
        self.name = name
        self.area = area
        self.free_area = area
        self.list = []
    def add(self,num_list):
        if num_list.list_area >90:
            return
        self.free_area -= num_list.list_area
        self.list.append(num_list.list_name)
    def __str__(self):
        return "%.2f --- %s " % (self.free_area,self.list)

my_list = HomeList("desk",80)
print(my_list)
my_house = House("两房一厅",90)
my_house.add(my_list)
print(my_house)