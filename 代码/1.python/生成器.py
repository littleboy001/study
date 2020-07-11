a = [x for x in range(10)]
print(a)
a = (x for x in range(10))#生成器用next生成，超出后会崩
#print(a)
for x in range (10):
	print(next(a))