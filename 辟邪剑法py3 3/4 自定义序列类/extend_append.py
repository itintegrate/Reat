#容器 list tuple deque
#扁平 str， bytes， bytearray array.array
#可变 list， deque bytearray array
#不可变 str， tuple， bytes

#if in  调用 container 魔法函数

from collections import abc

my_list = []
my_list.append(1)
my_list.append("a")


a = [1,2]
c = a+[3,4]
print(c)

#就地加
a += (3,4)
a += [3,4]
print(a)

#extend  没有返回值 可以做for循环 把每个值都加进来

a.extend(range(3))
a.extend((1,2))
print(a)


#append 没有for 循环 把整个list加进来
a.append((1,3))
print(a)