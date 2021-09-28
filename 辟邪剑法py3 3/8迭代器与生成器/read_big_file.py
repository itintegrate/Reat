from collections import UserList
#Userlist 和list 是一样的 唯一不同的是 UserList可以继承覆盖原函数  List 不可以
def myreadlines(f, newline):
  buf = ""
  while True:
    while newline in buf:
      #newline之前的所有值
      pos = buf.index(newline)
      #返回生成器， yield还可以继续往下走
      yield buf[:pos]
      #buf 覆盖断点之后所有的值
      buf = buf[pos+len(newline):]
    chunk = f.read(4096)

    if not chunk:
      yield buf
      break
    buf += chunk
    
with open("input.txt") as f:
  for line in myreadlines(f, "{|}"):
    print(line)