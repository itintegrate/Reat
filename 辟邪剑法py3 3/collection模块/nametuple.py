from collections import namedtuple #namedtuple 是创建一个类


#基本操作

User = namedtuple("User", ["name", "age", "height"])
user = User(name="bobby", age=29, height=175)
User.address = "Melbouren"
print(user.age, user.name, user.height, user.address)

#加入操作 
tuple_list = ("bobby", 29, 175)
dict_list = {"name":"bobby", "age":29, "height":175}

tuple_list_exc = ("bobby", 29, 175,"Melbourne")
dict_list_exc = {"name1":"bobby", "age":29, "height":175, "Address":"Melbourne"}

User2 = namedtuple("User2", ["name", "age", "height","Address"])
#加入操作tuple
#user2 = User2(*tuple_list,"Melbouren")

#加入操作dict
user2 = User2(**dict_list,Address="Melbourne")
print(user2)

#用_make加入 必要是正确的数量 不能多也不能少
user3 = User2._make(tuple_list_exc)
print(user3)

#用asdirct来转成OrderedDict形式
user_info_dict = user3._asdict()
print(user_info_dict)

#拆包
name, age, *other = user2
print(name, age, other) #other 是list形式
#*arg **karg
def ask(*arg, **karg):
  if arg:
    print(arg)
  else:
    print(karg)
  pass



ask("bobby", 29, 175)
ask(name="bobby", age=29, height=175)

