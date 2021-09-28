from collections import defaultdict

#找同样值 

users = ['booby1', 'bobby2', 'bobby3', 'bobby1', 'bobby1', 'bobby2']
user_dict = {}

#普通法
for user in users:
  if user not in user_dict:
    user_dict[user] = 1
  else:
    user_dict[user] += 1

print(user_dict)

#中间法 比普通法 高效 少一次查询

for user in users:
  user_dict.setdefault(user,0)
  user_dict[user] += 1

print(user_dict)

#高级法

default_dict = defaultdict(int) #也是可以放入list tuple string 放入int的初时值是0
for user in users:
  default_dict[user] += 1


#for loop dict 需要 两个值 dict。items（）
for index, value in default_dict.items():
  print(index, value)


#defalutdict 传一个dict进来

#先写个dict 函数

def group():
  groups = {
    "name":"",
    "num":0
  }
  return groups

default_dict_group = defaultdict(group)
default_dict_group["group1"]

for index, value in default_dict_group.items():
  print(index, value)


