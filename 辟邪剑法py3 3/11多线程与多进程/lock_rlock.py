#gil global interpreter lock （cpython）
#python中一个线程对应于c语言中的一个线程
#gil使得同一个时刻只有一个线程在一个cpu上执行字节码, 无法将多个线程映射到多个cpu上执行

#gil会根据执行的字节码行数以及时间片释放gil，gil在遇到io的操作时候主动释放
# import dis
# def add(a):
#     a = a+1
#     return a
# 
# print(dis.dis(add))
from threading import Lock, RLock


lock = Lock() #这是一把锁，整个程序就一把锁，整个程序就一把钥匙。
rlock = RLock() #这个可以多把锁， 但只能在一个线程里面用


total = 0

def add():
    #1. dosomething1
    #2. io操作
    # 1. dosomething3
    global total
    for i in range(1000000):
        lock.acquire() #关锁 锁被关了 必须要打开
        rlock.acquire()#关锁1 锁被关了 
        rlock.acquire()#关锁2 锁被关了 
        total += 3
        rlock.release()#开锁2 必须开锁否则不能向下执行
        rlock.release()#开锁1 必须开锁否则不能向下执行
        lock.release() #开锁 打开锁后才能再次申请关锁


def desc():
    global total
    for i in range(1000000):
        lock.acquire()
        total -= 3
        lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)

