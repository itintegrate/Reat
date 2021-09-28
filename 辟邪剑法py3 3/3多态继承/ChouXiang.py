
#抽象父类 主要是定义一些方法 在被继承的是 必须要调用

#方法一 定义CatchBase 的方法必须要调用 当创造对象不会有异常 但没有被覆盖方法会有异常

class CatcheBase():
  def get(self, key):
    raise NotImplementedError
  def set(self, key, value):
    raise NotImplementedError

class test1(CatcheBase):
  pass

#创造对象 不会报错
text1 = test1()
#会有异常 因为 get方法没有被重写
#text1.get("aaa")


#方法2 当创造对象的时候 如果没有被重写马上会有异常。

#抽象的import
import abc

class CacheBase2(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
      pass
    @abc.abstractmethod  
    def set(self, key, value):
      pass
class test2(CacheBase2):
  pass
#会有异常 因为 test2 没有被重写 抽象方法
text2 = test2()
