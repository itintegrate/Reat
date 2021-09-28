#切片模式【start：end：step】会返回新列表


"""
Start 切片的开始， 默认是0
end 切片的截止位置， 默认是列表长度， 是按总长值。 不是从0开始
当 start 为 0 是可以省略， end为列表长度页可以省了
当 step 为 1 是可以省， 也可以省列最后一个maohao
setp 为 负数 表示 相反切片， start 应该比 end 的值要大。

"""

alist = [3,4,5,6,7,9,11,13,15,17]
print(alist[::])#建立新列表
print(alist[::-1])#倒数list
print(alist[::2])#每两步取一个值
print(alist[1::2])#从第二个值开始 每两步取一个值
print(alist[3:6])#从第4元素 到第六个元素
print(alist[:100])#从0 开始 到100以下的截止点
print(alist[100:])#从100开始 如果没设为空


alist[len(alist):] = [9] #在最后添加一个zhi
alist[:0] = [1,2] #在第一个添加一个值， 类似于 alist = 【1，2】+ alist
alist[3:3] = [4] #在指定位置加一个值
alist[:3] = [1,2] #替换列表元素， 在等号两边要想等长度
alist[3:] = [4,5,5] #等号两边不需要想等 但会覆盖后面所有的值
alist[::2] = [0]*3 # [0]*3 是生产3个0， 页就是每两步换一个 0
alist[::2] = ['a', 'b', 'c']
alist[:4:2] = [1,2] #等号两边必须想等
alist[:3] = [] #删除列表前3个元素

del alist[:3] #删除前3ge

del alist[::2] #删除 每各一个



print(alist)



