#__getattr__ 是在查找不到属性的时候调用的：

#__getattribute__ 是最开始就用， 建议不要重写它


class User:
  def __init__(self, name, list_dic):
    self.name = name
    self.list_dic = list_dic

  def __getattr__(self, item):
    print(item)    
    return self.list_dic[item]

class User2:
  def __init__(self, name):
    self.name = name

  def __getattr__(self, item):
    print(item)    
    self.newname = item

user = User("aa",{"nameis":"wu"})
print(user.nameis) #nameis 就是 item

user2 = User2("aa")
print(user2.nameis) #nameis 就是 item

print(user2.newname)