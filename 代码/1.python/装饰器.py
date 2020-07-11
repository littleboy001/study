def w1(func):
	print("---1---")
	def inner():
		print("w1")
		func()
	return inner

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

f1()
