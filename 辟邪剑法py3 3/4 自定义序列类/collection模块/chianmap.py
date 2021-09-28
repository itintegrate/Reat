from collections import ChainMap

user_dict1 = {"a":"booby1", "b":"bobby2"}
user_dict2 = {"b":"booby3", "d":"bobby3"}

#正常的取值是

for k,v in user_dict1.items():
  print(k, v)

for k,v in user_dict2.items():
  print(k, v)

print("-----------------")


#chainmap 就是把多个dict 合成一个 dict 注意：只会出现第一次的重复值。 
new_dict = ChainMap(user_dict1,user_dict2)
#maps 就是把dict合成一个数组
print(new_dict.maps)
new_dict.maps[0]["a"] = "bobby"

for k,v in new_dict.items(): #ChainMap 只会出现第一次的重复值。 
  print(k, v)