from collections import OrderedDict
#dict有的方法他都有是dict的子类

user_dict = OrderedDict()
#user_dict = {"b":"bobby1", "a":"bobby2", "c":"bobby3"}
user_dict["b"] = "bobby2"
user_dict["a"] = "bobby1"
user_dict["c"] = "bobby3"

#user_dict.pop("a") # 删除key的值
#user_dict.popitem()# 删除最后一个值

user_dict.move_to_end("b") #把key值移到最后
print(user_dict)