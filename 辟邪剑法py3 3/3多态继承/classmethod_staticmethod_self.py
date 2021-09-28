class A():
  def __init__(self, p):
    print(p)

  def selfmethod(self):  #事例方法必须创造事例后调用
    print("I am selfmethod")

  @staticmethod #静态方法可以先生成
  def staticm():
    print(" i am in to staticmethod")
    

  @classmethod #类方法可以先生成要return个类
  def classm(cls, p):
    print(" i am in to classmethod")
    cls(p).selfmethod()
    return cls(p)
  
  def __str__(self):
    return "......."


a = A("ppp")
b = A.staticm()#调用一个静态函数
c = A.classm("pppppp")#可以调用当前的class
print("-----------")
a.selfmethod()

print(a)