#非常重要概念。 python里的多态是和类里面的方法有关 比如 3个类共同有一个同样的方法 这个三个类就可以是多态关系
# 这3个类共用一个 say() 这个三个类就可以是animal父类
class Cat():
    def say(self):
        print("i am a cat")

class Dog():
    def say(self):
        print("i am a dog")

class Duck():
    def say(self):
        print("i am a duck")
    def s(self):
        print("sss")

animal = Cat
animal().say()
#把前面三个类合成一个类 然后迭代他们的say（）方法。
animal2 = [Cat, Duck, Dog]
for each in animal2:
    each().say()



#举例 extend（）方法 extend方法是所以的迭代对象的综合。 他包括 list tuple set
class D():
 def __init__(self, d_list):
     self.d_list = d_list
 #有了getitem这个方法就是迭代类了 就可以用extend    
 def __getitem__(self, item):
     return self.d_list[item]


a = ["test1", "test2"]
b = ("test3", "test4")
c = set()
c.add("test5")
c.add("test6")
d = D(["test7","test8"])

#extend 方法综合了所以的迭代对象。 
a.extend(b)
print(a)
a.extend(c)
print(a)
a.extend(d)
print(a)