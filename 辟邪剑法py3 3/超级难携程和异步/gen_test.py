# -*- coding: utf-8 -*-
# @Author: jinpengwu
# @Date:   2020-02-27 08:33:50
# @Last Modified by:   jinpengwu
# @Last Modified time: 2020-02-27 08:38:05
def gen_func():
  html = yield "http://project.com"
  print(html)
  yield 2
  yield 3
  return "jin"

if __name__ == "__main__":
  # must use next(gen) or gen.send(None) at frist
  gen = gen_func()
  url = next(gen)
  #url = gen.send(None) #same like next(gen)
  html = "bobby"

  print(gen.send(html))