


#try catch fianlly
def try_except():
  try: #先试一试
    #f_read.open("xx.txt")
    print("code started")
    #raise KeyError
    #raise IndexError
    return 1
  except KeyError as e: #如果有已知错误
    print("Key Error")
    return 2
  else:#如果没有包以上错误 就来这里
    print("other Error")
    return 3
  finally:
    #最后的close（）
    print("finally")
    #f_read.close()
    return 4 #finally 会首先return。 如果没有return 就会return上面的except


#上下文管理器 也就是with语句和python __enter__ 与 __exit__ 的结合:

#举例。 先建立一个 包含 __enter__ 与 __exit__(self, exc_type, exc_val, exc_tb)的class

class WithSample():
  def __enter__(self):
    print("this is the enter function")

  def doSomething(self):
    print("this is main function")

  def __exit__(self, exc_type, exc_val, exc_tb):
    print("this is the exit function")

class WithSample2():

  def __init__(self, p):
    self.p = p

  def __enter__(self):
    print("this is the enter function")
    return self #这里要return 否则会报错

  def __exit__(self, exc_type, exc_val, exc_tb):
    print("this is the exit function")

  def do_something(self):
    print(self.p)



if __name__ == "__main__":

  print(try_except())

  #这里要用with语句去读取上下文协议的class：

  #写法一
  ws = WithSample()

  with ws:
    ws.doSomething()
    print("hhhahahahahahahahah")

  #写法二

  with WithSample2("fukc")as a:
    a.do_something()
    print("hhhahahahahahahahah")