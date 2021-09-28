#魔法函数不需要调用


class MagicsList():
    def __init__(self, employee_list):
        self.employee_list = employee_list

    #__str__ 魔法函数 可以让这个函数返回一个string
    # def __str__(self):
    #     return ",".join(self.employee_list)
    # 魔法函数不需要去召唤他。 解析器会在适当的时候调用他
    def __len__(self):
        return len(self.employee_list)
    
    def __str__(self):
        return "go fuck yourself"

company = MagicsList(['tom','bob','jane'])
print(len(company))
#返回一个值ç
print(company)

class MyVector():
    def __init__(self, x):
        self.x = x
    #__add__ 加上数字
    # def __add__(self,y):
    #     re_vector = MyVector(self.x+y)
    #     return re_vector

    # 加上另一个int类型的class
    def __add__(self,y):
        re_vector = MyVector(self.x+y.x)
        return re_vector

    def __str__(self):
        return "x:{x}".format(x=self.x)
my_vector = MyVector(2)
my_vector2 = MyVector(20)

print(my_vector+my_vector2)
