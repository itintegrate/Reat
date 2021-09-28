# -*- coding: utf-8 -*-
# @Author: jinpengwu
# @Date:   2019-11-06 00:02:20
# @Last Modified by:   jinpengwu
# @Last Modified time: 2019-11-06 00:09:48

class PrivatAtt(object):
  """docstring for PrivatAtt"""
  def __init__(self):
    #super(PrivatAtt, self).__init__()
    self.__arg = "aaaaa" #"__"是私有值。 事例不能调取， 只能在类里面使用
    self.argg = "bbbbbb"
  def get_arg(self):
    print(self.__arg) #用函数调取
    


if __name__ == '__main__':

    pa = PrivatAtt()
    pa.get_arg()
    #print（__arg）不能调取 报错
    print(pa.argg) 
    print(pa._PrivatAtt__arg) #破解私有函数 可以调取。