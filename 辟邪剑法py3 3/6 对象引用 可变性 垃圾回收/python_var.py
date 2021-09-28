#python 和java中的变量是不一样的。 python的变量实质上是个指针。 就像便利贴一样。

#举例

a = 1
a = "abc"
# 先生成对象 在加上a标签

b = a

#b 就是等用a 他们是同一个ID

print(id(b), id(a))


# == 与 is 的区别

a = [1,2,3]
b = [1,2,3]
#is 是判断 对象是否相等
print(a is b)

#== 是判断 值是否想等
print(a == b)