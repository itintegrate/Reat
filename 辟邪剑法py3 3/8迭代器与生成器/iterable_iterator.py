from collections.abc import Iterator


class Company(object):
  def __init__(self, employee_list):
    self.employee_list = employee_list

  def __getitem__(self, item):
    return self.employee_list[item]

  def __len__(self):
    return len(self.employee_list)

  def __iter__(self):
    return MyIterator(self.employee_list)

class MyIterator(Iterator):
  #继承Iterator 就会自动 __iter__()魔法方法

  def __init__(self, employee_list):
    self.iter_list = employee_list
    self.index = 0

  def __next__(self):
    #真正的迭代逻辑在这里
    try:
      word = self.iter_list[self.index]+"aaaa"
    except IndexError:
      raise StopIteration
    self.index += 1
    return word


if __name__ == "__main__":
  company = Company(["tom","bob","jane"])
  my_itor = iter(company)
  for item in my_itor:
    print(item)

  pass