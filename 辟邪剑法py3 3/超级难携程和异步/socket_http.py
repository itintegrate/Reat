import socket
from urllib.parse import urlparse

def get_url(url):

  url = urlparse(url) #urlparse 来解析url
  host = url.netloc #拿到host名
  print(host)
  path = url.path #拿到页面

  if path == "":
    path = "/"
  print(path)
  #建立socket连接  
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  client.setblocking(False) #页面非阻塞

  try:
    client.connect((host,80)) #建立连接
  except BlockingIOError as e:
    pass

  while True:
    try:
      client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode("utf8")) #发送请求
      break
    except OSError as e:
      pass

  data = b""
  while True:
    try:
      d = client.recv(1024) #接到请求
    except BlockingIOError as e:
      continue
    if d:
      data += d
    else:
      break
  data = data.decode("utf8")
  print(data)
  client.close()

if __name__ == "__main__":
  import time
  start_time = time.time()
  for url in range(20):
    url = "http://shop.projectsedu.com/goods/{}/".format(url)
    get_url(url)
  print(time.time()-start_time)