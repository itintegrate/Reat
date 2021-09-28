#对于io操作来说， 多线程和多进程性能差距不大
#1。通过Thread类实例化

import time
import threading

#方法一 比较老 不建议用 只是用来理解

t_list = []

def get_detail_html(t_list):
  while True:
    time.sleep(3)
    if len(t_list) > 0:
      url = t_list.pop()
      print(url+"i am in")
    else:
      break;


def get_detail_url(t_list):
      print("get detail url started")
      for i in range(20):
        t_list.append("http://aaa/{}".format(i))        
      print("get detail url ended")

    




if __name__ == "__main__":
  f1 = threading.Thread(target=get_detail_url,args=(t_list,))
  f1.start()
  print(len(t_list))

  for i in range(10):
    f2 = threading.Thread(target=get_detail_html,args=(t_list,))
    f2.start()
  
  f1.join()
  


