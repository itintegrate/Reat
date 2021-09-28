from collections import deque
import copy

#deque 和 list是一样的 就是功能多了些。比如可以 appendleft 等
#deque GIL锁线程安全的 ， list不是线程安全的



user_deque = deque(["bobby1", ["bobby2", "bobby3"], "bobby3"])
#向左插入一个值
user_deque.appendleft("bobby4") #只是更改不生成新对象

#浅copy值拷贝元素
user_deque2 = user_deque.copy()
user_deque2[1] = "vvvvbobby1" #元素不会改变
user_deque2[2].append("bobby1") #append会改变
print(id(user_deque), id(user_deque2))
print(user_deque, user_deque2)
print(user_deque)

#深copy完全copy
user_deque3 = copy.deepcopy(user_deque)

#合并连个deque 用 extend
user_deque2.extend(user_deque3) #只是更改不生成新对象


#插入点deque 用insert
user_deque2.insert(0, "jinpengwu") #只是更改不生成新对象

#反转 deque 用reverse
user_deque2.reverse()  #只是更改不生成新对象

print(user_deque2)

