#用 @property来封装函数，用attrs调用出来例如：


class User:
  def __init__(self):
    pass


  #先set property 封装函数。 property相当是get
  @property
  def age1(self): 
    return 2019 - self.year

  #再用 setter。 setter 相当是set
  @age1.setter #在 age1 的propety中。用函数age3来set year
  def age1(self, year):
    self.year = year
    



user = User()
user.age1 = 1985 #age1 的 setter year 是1985
print(user.age1)# age1 的返回 34 