#python 垃圾回收的算法是 采用 引用计数

a = "aaa" #引用计数为1

b = a #引用计数 加 1 一共是2

del(a)#引用计数减 1 还有一个

print(b) #所以 b可以打印出来
  