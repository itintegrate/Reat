#对于io操作来说， 多线程和多进程性能差距不大
#1。通过Thread类实例化

import time
import threading
from queue import Queue

#方法一 比较老 不建议用 只是用来理解

t_list = []

def get_detail_html(t_list):
  while not t_list.empty():   
      time.sleep(3)
      url = t_list.get()
      print(url+"i am in")
      print(t_list.qsize())
      t_list.task_done()
 
      



def get_detail_url(t_list):
      print("get detail url started")
      for i in range(5):
        t_list.put("http://aaa/{}".format(i))        
      print("get detail url ended")

    




if __name__ == "__main__":


  detail_url_queue = Queue(maxsize = 1000)

  f1 = threading.Thread(target=get_detail_url,args=(detail_url_queue,))
  f1.start()
  


  f2_ths = []
  for _ in range(3):
    f2 = threading.Thread(target=get_detail_html,args=(detail_url_queue,))
    f2_ths.append(f2)
    f2.start()
  
  

  
 
  
  detail_url_queue.join()  
  print("hhh")
  f1.join()
  for f2_th in f2_ths:
     print("aaaaa")
     f2_th.join()
  
 


