class Test(object):
	def __init__(self):
		self.__num =100
	def set_num(self,num):
		print("setter")
		self.__num = num
	def get_num(self):
		print("getter")
		return self.__num
	num = property(get_num,set_num)


test = Test()
print(test.num)

"""
print(test.get_num())
print("----")
test.set_num(50)
print(test.get_num())

"""
print("---")
test.num =200
print("----")
print(test.num)


"""
a = [x for x in range(10)]
print(a)



def num(a,b,c):
	return c(a,b)
print(num(11,22,lambda x,y:x+y))
"""