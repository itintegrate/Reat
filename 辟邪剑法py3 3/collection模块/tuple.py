
#tuple 是不可变的 == （）

#tuple 好处：
#1. 性能youhua
#2. 线程安全
#3. 可以作为dict的key
#4. 拆包特性

name_list = ("bobby1", "bobby2")

user_tuple = ("booby", 29, 175)

#会报错 tuple是不可变得
#name_list[0] ="bobby3"

#空tuple是 
empty_tuple = ()
#or
empty_tuple2 = "",
print(type(empty_tuple))
print(type(empty_tuple2))

#tuple的拆包


#全拆
name, age, height, *other1 = user_tuple

print(name, age, height, other1)

#限拆
name2, age2, height2 = user_tuple

print(name2, age2, height2)

#分拆
name1, *other= user_tuple

print(name1, other)



#可以作为dict的key：
user_tuple_dict = {}
user_tuple_dict[user_tuple] = "testing...."

print(user_tuple_dict)


for each in name_list:
  print(each)