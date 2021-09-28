
#多用isinstance 少用 type
#isinstance 返回的是 boolen
#type 返回的是 对象的 Type

# is 来判断是不是一个duixiang
# == 是判断是值是否想动
#xx.__base__ 是来找到继承父类


#id()是来找到对象的id


class A:
  pass
class B(A):
  pass

b = B()

print(isinstance(b,B))

print(type(b))
print(B.__base__)
print(type(A))