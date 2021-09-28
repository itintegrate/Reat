class Company(object):
	"""docstring for Company"""
	def __init__(self, employee_list):
		self.employee_list = employee_list
	""" 魔法函数 把 class 转换成 list模式"""
	def __getitem__(self, item):
		return self.employee_list[item]
	""" 魔法函数 可以用len（）展示list的数量"""	
	def __len__(self):
		return len(self.employee_list)

#现在的company 就是list模式
company = Company(['tom', 'boby', "jane"])
#company = Company("aabbcc")

#也可以用切片函数
company1 = company[:2]

#for loop 使用
for each in company1:
	print(each)
#显示出来company的list class的数量
print(len(company))