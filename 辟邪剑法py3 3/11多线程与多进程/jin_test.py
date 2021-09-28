#对于io操作来说， 多线程和多进程性能差距不大
#1。通过Thread类实例化

import time
import threading

class run1(threading.Thread):
  def __init__(self,name):
    super().__init__(name=name)

  def run(self):
    for each in range(300):
      print("I am in Run 1 -- {}".format(each))

    print("Run 1 finished")



class run2(threading.Thread):
  def __init__(self,name):
    super().__init__(name=name)

  def run(self):
    for each in range(300):
      print("I am in Run 2 -- {}".format(each))

    print("Run 2 finished")


if __name__ == "__main__":
  #主线程
  #thread1 = threading.Thread(target=get_detail_html, args=("",))
  #thread2 = threading.Thread(target=get_detail_url, args=("",))

  r1 = run1("run1")
  r2 = run2("run2")





 
  r1.start()
 
  r2.start()


  #join是杜塞在这里 必须等现代完成
  r1.join() #如果没有join 线程会一直执行 即便主程序关闭。 非常危险  
  r2.join()
  print("deng.........")


