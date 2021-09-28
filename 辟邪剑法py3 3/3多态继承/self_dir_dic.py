#通过一定的机制查询内部结构



class Person:
  name = "user"

class Student(Person):
  def __init__(self, school_name):
    self.school_name = school_name

if __name__ == "__main__":
  user = Student("Imooc")

  #通过__dict__查询属性只会找到当前的类内容 不查找继承的父类 而切它只能找类。
  print(user.__dict__)
  #通过__dict__找到所以Person下的函数
  print(Person.__dict__)
  #通过__dict__加载新的的函数
  user.__dict__["school_address"] = "Melbourne"
  print(user.__dict__)
  print(user.school_address)

  #通过dir也可以找到类里所有的函数名:可以找类也可以找函数
  print(dir(user))
  print(dir(Person))
  print(dir(['1','2']))

  print(user.name)