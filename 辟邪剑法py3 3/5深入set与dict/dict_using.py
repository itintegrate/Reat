a = dict()

a = {"bobby1":{"company":"imooc"}, 
    "bobby2":{"company":"imooc2"}
    }
print(a)
#a.clear() #清空dict
# print(a) 


#copy ， 返回的是浅copy
#浅copy 重写原来的dict

new_dict = a.copy()
new_dict["bobby1"]["company"] = "imooc3"

print(new_dict)
print(a) #被重写


import copy

#深copy 要import copy 包

new_dict_deep = copy.deepcopy(a)
new_dict_deep["bobby1"]["company"] = "imooc6"

print(new_dict_deep)
print(a) 


#fromkeys
new_list = ["bobby1", "bobby2"]
new_dict2 = dict.fromkeys(new_list, {"company":"imooc1", "company":"imooc2"})
print(new_dict2)

#dict 的 get方法 传两个参数 一个是 key 如果key找到 就返回key值， 第二是 默认值。 如果没有找到可以 就会返回默认值
value = new_dict.get("bobby1", {})
print(value)

#items 查找

for key, value in  new_dict.items():
  print(key, value)


#setdefault 添加新的dict

default_value = new_dict.setdefault("bobby","imooc")
print(default_value)
print(new_dict)  

#upate 更新一个新dict 4种方法
new_dict.update(bobby="imssss")
print(new_dict)

new_dict.update((("bobby","imsss2222"),))
print(new_dict)

new_dict.update([("bobby","imsss33333")])
print(new_dict)

new_dict.update({"bobby":"imooc7777"})
print(new_dict)



