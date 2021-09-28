#列表生产式
#1， 提取1-20 之前的奇数

#正常方法
odd_list=[]
for i in range(21):
  if i%2  == 1:
    odd_list.append(i)

#简写法

odd_list = [i for i in range(21) if i%2 == 1]

#在数组里写逻辑 分三段  1 值， 2 逻辑 3 判断

def sqa(item):
  return item*item

odd_list = [sqa(i) for i in range(21)]

print(odd_list)



#生成器表达式
odd_gen = (i for i in range(21) if i%2 == 1) #把中括号 变成小括号 你成了生成器。生成器是个objct

print(odd_gen) #看不到值， 是个object

# for each in odd_gen:
#   print(each)

odd_list2 = list(odd_gen)
print(odd_list2)


#字典推到式
#正常方法
my_dict = {"bobby1":22, "bobby2":23, "imooclcom":5}

#简单法
reversed_dict = {value:key for key, value in my_dict.items()}
print(reversed_dict)

#集合推到式
#正常方法
my_set = set(my_dict.keys())

#简易法 可以加入逻辑
#my_set= {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)