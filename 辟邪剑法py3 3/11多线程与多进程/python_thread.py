#对于io操作来说， 多线程和多进程性能差距不大
#1。通过Thread类实例化

import time
import threading

def get_detail_html(url):
  print("get detail html started")
  time.sleep(6)
  print("get detail html ended 1")

def get_detail_url(url):
  print("get detail url started")
  time.sleep(4)
  print("get detail url end 2")


#类线程的实现 比较实用
class GetDetailHtml(threading.Thread):
  def __init__(self,name):
    super().__init__(name=name)

  def run(self):
      print("get detail html started")
      time.sleep(2)
      print("get detail html ended 1")

class GetDetailUrl(threading.Thread):
  def __init__(self,name):
    super().__init__(name=name)

  def run(self):
      print("get detail html started")
      time.sleep(6)
      print("get detail html ended 2")


if __name__ == "__main__":
  #主线程
  #thread1 = threading.Thread(target=get_detail_html, args=("",))
  #thread2 = threading.Thread(target=get_detail_url, args=("",))

  thread1 = GetDetailHtml("get_detail_html")
  thread2 = GetDetailUrl("get_detail_url")
  start_time = time.time()


  #当主线程退出的时候， 子线程kill 掉
  #setDaemon True 当主线程退出 子线程也退出。
  #但如果有了join方法 setDaemon 就没有意义了 因为 join一定哟啊执行完才会退出
  thread1.setDaemon(True) 
  thread2.setDaemon(True)


  #这里共3个线程 
  #线程1
  thread1.start()
  #线程2
  thread2.start()


  #join是杜塞在这里 必须等现代完成
  thread1.join() #如果没有join 线程会一直执行 即便主程序关闭。 非常危险  
  thread2.join()
  print("deng.........")



  print("{}".format(time.time()-start_time))

