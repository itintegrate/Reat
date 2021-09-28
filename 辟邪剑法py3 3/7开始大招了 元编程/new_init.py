#__new__(cls, *args, **kargs) new是用来生成对像之前的过程。。 在对象生成qian
#__init__(self) init 是完善对象的ß
#如果 new方法不返回对象。 则不会调用init




class test:
  def __new__(cls, *args, **kargs):
    print("i am new")
    #new方法不返回对象。 则不会调用init
    return super().__new__(cls)

  def __init__(self, name):
    print("i am init")
    self.name = name


tt = test("aaa")
