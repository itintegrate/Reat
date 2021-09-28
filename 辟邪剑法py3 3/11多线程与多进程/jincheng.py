# -*- coding: utf-8 -*-
# @Author: jinpengwu
# @Date:   2020-02-04 07:35:58
# @Last Modified by:   jinpengwu
# @Last Modified time: 2020-03-06 07:34:49

def fib(n):
  if n<=2:
    return 1
  return fib(n-1)+fib(n-2)
from concurrent.futures import ThreadPoolExecutor, as_completed #多线程
from concurrent.futures import ProcessPoolExecutor, as_completed #多进程
import time

# cup 的操作
# if __name__ == "__main__":
#   with ProcessPoolExecutor(3) as executor: #多进程 快
#   with ThreadPoolExecutor(3) as executor: #多线程 慢
#     all_task = [executor.submit(fib, (num)) for num in range(25, 30)]
#     start_time = time.time()
#     for futures in as_completed(all_task):
#       data = futures.result()
#       print("get {} page".format(data))

#     print("last time is: {}".format(time.time()-start_time))

# io 的操作

def random_sleep(n):
  time.sleep(n)
  return n


if __name__ == "__main__":
  #with ProcessPoolExecutor(30) as executor: #多进程 慢

  #clean write:
  
  # def ex_sub():
  #   all_task = []
  #   for num in [2]*30:
  #      all_task.append(executor.submit(random_sleep,(num)))
  #      all_task.append(executor.submit(lambda p: random_sleep(*p), [arg1， arg2]))  #传多惨
  #        
  #   return all_task

  # with ThreadPoolExecutor(30) as executor:  #多线程 快
  #   all_task = []
  #   start_time = time.time()
  #   for futures in as_completed(ex_sub()):
  #     data = futures.result()
  #     print("get {} page".format(data))



  with ThreadPoolExecutor(30) as executor:  #多线程 快
    all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
    #all_task = [executor.submit(lambda p: random_sleep(*p), [arg1， arg2]) for num in [2]*30] # 传多参数
    
    start_time = time.time()
    for futures in as_completed(all_task):
      data = futures.result()
      print("get {} page".format(data))

    print("last time is: {}".format(time.time()-start_time))