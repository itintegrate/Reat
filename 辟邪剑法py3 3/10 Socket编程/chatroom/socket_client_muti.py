import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


#用selector来非阻塞 形成

selector = DefaultSelector()

class CliSide:

  def connected(self, key):

      re_data = input()
      self.client.send(re_data.encode("utf8"))




  def cliMain(self):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client.setblocking(False)

    try:
      self.client.connect(('127.0.0.1',8000))
    except BlockingIOError as e: 
        pass
       
    selector.register(self.client.fileno(), EVENT_WRITE, self.connected)       

def loop():
  while True:
    #先取出selctor中注册的方法s
    ready = selector.select()
    for key, mask in ready:
      call_back = key.data
      call_back(key)

if __name__ == "__main__":
  clsi = CliSide()
  clsi.cliMain()
  loop()