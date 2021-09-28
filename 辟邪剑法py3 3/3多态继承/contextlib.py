#这个是简化的上下文生成器

#第一 要 import contextlib

import contextlib

def entery():
  print("staring.. function")

def close():
  print("closeing.. function")

def working():
  print("working......")

@contextlib.contextmanager
def file_open(tst):
  entery()
  yield # 这个就是生成器 在 yield 上面是 Entery 功能 yield下面是 close功能
  close()


with file_open("aaaa") as f:
  working()