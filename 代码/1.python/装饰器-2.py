def w1(func):
	print("---1---")
	def inner(*args,**kwargs):
		print("w1")
		ret = func(*args,**kwargs)
		return ret
	return inner
"""
def w2(func):
	print("---2---")
	def inner():
		print("w2")
		func()
	return inner
@w1 #f1 = w1(f1)
@w2 #f1 = w2(f1)
def f1():
	print("---f1---")
"""
@w1
def f2(a,b,c):

	print("f2")
	return "haha"

#f1()
a=f2(11,22,33)
print("%s"%a)