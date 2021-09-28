class A:
  #没有写self在前面 是全局值
  aa = 1 #全局的aa
  def __init__(self, x, y):
    self.x = x
    self.y = y

a = A(2,3)
b = A(4,6)
c = A(7,8)
a.aa = 100
A.aa = 50
b.aa = 30

#b.aa 是 A（）创造的事例b aa是事例下的值
print(b.aa)
print(a.aa)
#c.aa 是 A（）创造的事例b aa没有重写所以 aa要用全局的aa值 50
print(c.aa)
#A没有创建对象。所以A.aa 就是全局的aa
print(A.aa)