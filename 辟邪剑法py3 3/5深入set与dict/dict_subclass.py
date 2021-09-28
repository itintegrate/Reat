#不建议继承listh和dict 容易出错

#如果真要继承Dirct using from collections import UserDict

from collections import UserDict


class Mydict(UserDict):
  def __setitem__(self, key, value):
    super().__setitem__(key, value*2)

my_dict = Mydict(one=1)

print(my_dict["one"])


from collections import defaultdict #会加个空的值或者0

my_dict = defaultdict(list)
my_dict["aaa"] 
print(my_dict)