import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))
server.listen()


#从客户端发送的数据
#一次获取1k数据
while True:
  sock, addr = server.accept()

  data = sock.recv(1024)
  print(data.decode("utf8"))
  #sock.send("hello {}".format(data.decode("utf8")).encode("utf8"))
  re_data = input()
  sock.send(re_data.encode("utf8"))

#server.close()
#sock.close()