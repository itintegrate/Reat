#什么是迭代
#迭代器是访问集合内元素的一种方式， 一般用来遍历数据
#迭代器与一下访问方式不一样， 迭代器是不能返回的

#【】list， __iter__ 是有迭代功能
#迭代器是 __iter__ 和 __next__ 两个魔法函数


from collections.abc import Iterable, Iterator
a = [1,2]

#【】list， __iter__ 是有迭代功能
print(isinstance(a, Iterable))

#【】list， __iter__ 但是没有 __next__  不是有迭代器
print(isinstance(a, Iterator))


iter_ator = iter(a) #转化成迭代器

#iter(a)， __iter__ 和 __next__  是有迭代器
print(isinstance(iter_ator,Iterator))