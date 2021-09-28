import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


#用selector来非阻塞 形成

selector = DefaultSelector()

urls = []
stop = False

class Fetcher:
  def connected(self, key):
      selector.unregister(key.fd)
      self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path,self.host).encode("utf8")) #发送请求
      selector.register(self.client.fileno(), EVENT_READ, self.readable)
  
  def readable(self,key):
      d = self.client.recv(1024) #接到请求
      if d:
        print(d)
        self.data += d
      else:
        selector.unregister(key.fd)
        self.data = self.data.decode("utf8")
        print(self.data)
        self.client.close()
        urls.remove(self.full_url)
        if not urls:
          global stop
          stop = True



  def get_url(self, url):
      self.full_url = url
      url = urlparse(url) #urlparse 来解析url
      self.host = url.netloc #拿到host名
      print(self.host)
      self.path = url.path #拿到页面
      self.data =b''

      if self.path == "":
        self.path = "/"
      print(self.path)
      #建立socket连接  
      self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
      self.client.setblocking(False) #页面非阻塞

      try:
        self.client.connect((self.host,80)) #建立连接
      except BlockingIOError as e: 
        pass

      #selecr中的注册  
      selector.register(self.client.fileno(), EVENT_WRITE, self.connected)  
      
        


def loop():
  while not stop:
    #先取出selctor中注册的方法s
    ready = selector.select()
    for key, mask in ready:
      call_back = key.data
      call_back(key)

if __name__ == "__main__":

  #fetcher = Fetcher()
  import time
  start_time = time.time() 
  for url in range(20):
    url = "http://shop.projectsedu.com/goods/{}/".format(url)
    urls.append(url)
    fetcher = Fetcher()
    fetcher.get_url(url)
  loop()  
  print(time.time()-start_time)    


# def get_url(url):

#   url = urlparse(url) #urlparse 来解析url
#   host = url.netloc #拿到host名
#   print(host)
#   path = url.path #拿到页面

#   if path == "":
#     path = "/"
#   print(path)
#   #建立socket连接  
#   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
#   client.setblocking(False) #页面非阻塞

#   try:
#     client.connect((host,80)) #建立连接
#   except BlockingIOError as e:
#     pass

#   while True:
#     try:
#       client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode("utf8")) #发送请求
#       break
#     except OSError as e:
#       pass

#   data = b""
#   while True:
#     try:
#       d = client.recv(1024) #接到请求
#     except BlockingIOError as e:
#       continue
#     if d:
#       data += d
#     else:
#       break
#   data = data.decode("utf8")
#   print(data)
#   client.close()

# if __name__ == "__main__":
#   get_url("http://www.baidu.com")

