from collections import deque
from collections import Counter

#Counter 是来用统计的次数

user_deque = deque(["bobby1", "bobby2", "bobby3", "bobby3", "bobby1", "bobby2", "bobby3", "bobby3", "bobby1", "bobby2", "bobby3", "bobby3"])
string_word = "xfds3rsdfsdfsdfkwejriowesfdkllkdsaklofhsdkaljfsdlkfsdklfnsdklfjiweroisfdkljfskdafklsdnfksdfjklsdfjklsd"
#Counter 正常统计的次数
user_counter = Counter(user_deque)
string_conter = Counter(string_word)
#Counter 添加统计的次数
user_counter.update(string_conter) #只是更改不生成新对象

#Counter 出现最多的前几名
print(user_counter.most_common(5))



print(string_conter)
print(user_counter)


