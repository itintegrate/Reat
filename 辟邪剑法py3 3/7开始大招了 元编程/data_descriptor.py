#在一个class里面如果有 __get__(self, instance, owner) , __set__(self, instance, value), __delete__(self, instance)任何一个协议 都是属性描述符

#数据描述符举例：

import numbers

class IntField:
  def __get__(self, instance, owner):
    return self.age
    pass

  def __set__(self, instance, value):
    
    if not isinstance(value, numbers.Integral):
      raise ValueError("int value need")

    if value <0 :
      raise ValueError("must greater than 0")
    self.age = value

    pass

  def __delete__(self, instance):
    pass

#非数据描述符
class NoneDataDes:
  def __init__(self):
    self.no_data_des = 666666
  def __get__(self, instance, owner):
    return self.no_data_des


class User:
  age = IntField()
  no_data_des = NoneDataDes()



user = User()
user.age = 30

print(user.age)
#user.age另一种写法
print(getattr(user,'age'))

print(getattr(user,'no_data_des'))

#查找顺序
#1 如果 类 User 里面的age 是 数据描述符 那个它的优先级最高
#2 如果 lei生成对象 user 里面的age 是第二个调用
#3 非数据描述符
#4 属性描述符
