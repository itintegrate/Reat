#set 是集合， fronzenset（不可变集合）无序， 不重复
#set 性能很高

S = set("adfsdfsfadfsfsdfsfsdfsdfsdfsdfsdfsdfdsfsdfsfadfsdfsd") #结果是不重复的

s = set(["a","b","c","d","e"])
print(S)
print(s)


#set 的简写模式

ss = {"a","b","c"} #无序去掉重复
# ss.add("xxx") #可以加值

ss.update(set("cef"))#合并值 但不可重复

re_set = ss.difference(set("cef")) #在set("sdfsdfsdf")不存在的SS的 ss值
print(re_set)

#同样可以
another_set = set("cef")
re_set2 = ss - set("cef") #没有重复的
re_set2 = ss & another_set #找出共同的值
re_set2 = ss | another_set #合并去重


print(re_set2)


print("--------------------")
print(ss)


#frozenset 是不可变的 不可以加值。 所以可以作为 dict的key

s2 = frozenset("abcd")
print(s2)


if "c" in re_set2: #可以用in来查找

  print("I am in")

print(ss)
print(ss.issubset(re_set2)) #re_set2.有没有给ss做过运算