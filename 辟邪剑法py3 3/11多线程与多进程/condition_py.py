import threading
import time


class XiaoAi(threading.Thread):
  """docstring for XiaoAi"""
  def __init__(self, cond):
    super().__init__(name="xiaoAi")
    self.cond = cond

  def run(self):
    with self.cond:
      self.cond.wait()
      time.sleep(2)
      print("{}: hi TianMao".format(self.name))
      self.cond.notify()
      self.cond.wait()
      time.sleep(2)
      print("{}: Fine Thank you, and you ?".format(self.name))
      self.cond.notify()



class TianMao(threading.Thread):
  """docstring for XiaoAi"""
  def __init__(self, cond):
    super().__init__(name="tianMao")
    self.cond = cond

  def run(self):
    with self.cond:

      print("{}: hi XiaoAi".format(self.name))
      self.cond.notify()
      self.cond.wait()

      print("{}: How are you ?".format(self.name))
      self.cond.notify()
      self.cond.wait()

      print("{}: I am fine too".format(self.name))
      self.cond.notify()
      self.cond.wait()


class XiaoAi2(threading.Thread):
  """docstring for XiaoAi"""
  def __init__(self, cond):
    super().__init__(name="xiaoAi2")
    self.cond = cond

  def run(self):
    with self.cond:
      self.cond.wait()
      time.sleep(1)
      print("{}: hi TianMao2".format(self.name))
      self.cond.notify()
      self.cond.wait()
      time.sleep(1)
      print("{}: Fine Thank you, and you ?2".format(self.name))
      self.cond.notify()


if __name__ =="__main__":
  cond = threading.Condition()
  xa = XiaoAi(cond)
  xa2 = XiaoAi2(cond)
  tm = TianMao(cond)

  xa2.start()
  xa.start()

  tm.start()