# -*- coding: utf-8 -*-
# @Author: jinpengwu
# @Date:   2019-11-08 13:13:41
# @Last Modified by:   jinpengwu
# @Last Modified time: 2019-11-08 17:52:32


#mixin 模式特点
#1. Mixin类的功能单一
#2. buhe父类关联， 可以和任何父类组合
#3. Mixin中不要调用super（）

#mixin

class testMixin():

  def test_one_fun(self):
    print("only one function")
    fn = "only one function"
    return fn

class test2Mixin():

  def test_two_fun(self):
    print("only one function 2")
    fn = "only one function 2"
    return fn

class JichengMixin( testMixin, test2Mixin):
    print("haha")


if __name__ == "__main__":
  jx = JichengMixin()
  jx.test_two_fun()
  jx.test_one_fun()
