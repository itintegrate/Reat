import threading
import time

class setup2(threading.Thread):
  """docstring for setup2"""
  def __init__(self, url, sem):
    super().__init__()
    self.sem = sem
    self.url = url

  def write_to_file(self,data):
      with open('t.csv', 'a', encoding ="utf-8-sig") as f:
          f.write(data + '\n')

  def run(self):
    self.sem.acquire()
    time.sleep(2)
    print("got html")
    self.url = self.url.replace("xxx","google")
    self.write_to_file(self.url)

    self.sem.release()




class setup1(threading.Thread):
  """docstring for setup2"""
  def __init__(self, sem):
    super().__init__()
    self.sem = sem

  def run(self):
    for i in range(20):
      html_thread = setup2("http://xxx.com/{}".format(i),sem)
      html_thread.start()


if __name__ == '__main__':

 sem = threading.Semaphore(20)
 s2 = setup1(sem)
 s2.start()

    