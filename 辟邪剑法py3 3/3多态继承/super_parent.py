class A:
  def __init__(self):
    print("A")

class B(A):
  def __init__(self):
    print("B")
    #这个是python2的调用父类
    #super(B, self).__init__()
    super().__init__()


#当复杂的情况下 super就有用了 比如
#在这个多线程下 Thread的init已经有了Name属性。 所以可以直接传递进去
from threading import Thread
class MyThread(Thread):
  #先写自己的init把该写的值带进来
  def __init__(self, name, user):
    #在把那么name传会给父类（Thread）就可以了 因为Tread里面也用name
    super().__init__(name=name)

#super 不是直接调用父类。 是mro算法顺序：

class A1:
  def __init__(self):
    print("A")

class B1(A1):
  def __init__(self):
    print("B")
    super().__init__()

class C1(A1):
  def __init__(self):
    print("C")
    super().__init__()

class D1(B1, C1):
  def __init__(self):
    print("D")
    super(D1, self).__init__()

if __name__ == "__main__":
  #b = B()
  d = D1()
  print(D1.__mro__)
  #这里面MRO的顺序 继承是根据MRO顺序的
  
  #(<class '__main__.D1'>, <class '__main__.B1'>, <class '__main__.C1'>, <class '__main__.A1'>, <class 'object'>)