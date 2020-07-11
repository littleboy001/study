def func():
	a,b=0,1
	for x in range(10):
		yield b
		a,b = b,a+b
a=func()

print(next(a))
print(next(a))
print(next(a))
print(next(a))   #next(a)相当于a.__next__()

#for x in a:
#	print(x)