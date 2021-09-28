import numbers
class Group:
  #自制一个支持切片的组 (sequance)

  def __init__ (self, group_name, company_name, staffs):
    self.group_name = group_name
    self.company_name = company_name
    self.staffs = staffs

  #必须要的一下协议：

  def __reversed__(self):
    self.staffs.reverse()

  # def __getitem__(self, item): #实现切片的关键 
  #   pass

  def __getitem__(self, item):

    cls = type(self)
    if isinstance(item, slice):
      return cls(self.group_name, self.company_name, self.staffs[item])
    elif isinstance(item, numbers.Integral):
      return cls(self.group_name, self.company_name, [self.staffs[item]])



  def __len__(self):
    return len(self.staffs)
  def __iter__(self):
    return iter(self.staffs)
  def __contains__(self, item):
    if item in self.staffs:
      return True
    else:
      return False


gp_staffs = Group("imooc_jin", "imooc", ["bobby1", "bobby2", "bobby3", "bobby4"])
gp_staffs = Group("imooc_jin", "imooc", [1, 2, 3, 4])
print(type(gp_staffs))
for each in gp_staffs:
  print(each)