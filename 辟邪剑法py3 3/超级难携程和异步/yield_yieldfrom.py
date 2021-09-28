# -*- coding: utf-8 -*-
# @Author: jinpengwu
# @Date:   2020-02-28 08:31:39
# @Last Modified by:   jinpengwu
# @Last Modified time: 2020-02-28 09:05:35

from itertools import chain

def my_chain(*args, **kwargs):
  for each in args:
    for each2 in each:
      yield each2

def my_chain_yield_from(*args, **kwargs):
  for each in args:
    # for each2 in each:
    #   yield each2
    print("this is yield from")
    yield from each      
#data = dict(test1 = ['aa','bb','cc'],test2 = {'testdict1':'aa.com','testdict2':'bb.com'},)
my_list = [1,2,3]
my_dict = {"bobby1":"http://projectedu.com",'bobby2':"http://www.imoc.com"}



# for value in chain(my_list,my_dict,range(5,10)):
#   print(value)

for value in my_chain_yield_from(my_list,my_dict,range(5,10)):

  print(value)

# yield 传进去什么，就输出什么
def gi(itre):
  yield itre

# yield from 转进去itre 就会l输出itre的值
def g2(itre):
  yield from itre

for each in gi(range(10)):
  print(each)

for each2 in g2(range(10)):
  print(each2)


