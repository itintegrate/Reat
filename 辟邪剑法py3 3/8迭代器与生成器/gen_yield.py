from collections.abc import Iterator

#生成器就是函数里面有yield关键字
def gen_func():

  #yield的几个特性 1. 有了yield他的函数就会变成对象， 2. yield可以继续往下走不会end。 3. 可以多个yield.  4有了yield 就可以 forloop
  yield 1
  yield 2
  yield 3

  print("hahaha i am lasst")



gen_yield = gen_func()

for each in gen_yield:
  print(each)




def test_gen(index):
  n = 0
  while n<index:
    print(n + 1)
    yield index
    n +=1


a = test_gen(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

for each in a:
  pass