#类也是对象， type创建类的类

#用 def 动态创建 class
def create_class(name):
  if name == "user":
    class User:
      def __str__(self):
        return "user"
    return User
  elif name == "company":
    class Company:
      def __str__(self):
        return "company"
    return Company

#用type 来创建类
#User = type("User",(),{})

class baseclass():
  print("I am baseclass")
  def answer(self):
    return "i am baseclass {}".format(self.say)


def say(self, age): #要加self
  self.age = age
  return self.age


#什么事元类。 元类就是创建类的类。 type就是元类 顺序是  type创建了类， 类创建了对象  所以元类要继承type

#python中类的实例化过程， 会首先寻找metaclass 同过metaclass 包括父类 创建 user


class MetaClass(type):
  def __new__(cls, *args, **kwargs):
    return super().__new__(cls, *args, **kwargs)

  

class User3(metaclass = MetaClass):
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return "user {}".format(self.name)



#if __name__ == "__main__":
# MyClass = create_class("user")
# my_class = MyClass()
# print(my_class)
#用type 来创建类加属性

myUser = type("User",(),{"name":"bobby"})
myu = myUser()
print(myu.name)

#用type来创建function, 和继承


myUser2 = type("User2",(baseclass,),{"name":"bobby", "age":"33", "say":say}) #加继承一定要有逗号 因为它是tuple type创建了类 myUser2
myu2 = myUser2() #myUser2 创建了对象 myu2
print(myu2.name)
print(myu2.say("77"))
print(myu2.answer())

myu3 = User3("bobby")
print(myu3)


