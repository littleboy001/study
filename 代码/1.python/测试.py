#print(12**2)
#print(12^2)
"""
a= (x for x in range(0,10,2))

print(next(a))
print(next(a))
print(next(a))
print(next(a))
"""
a = range(10)
print(a)
print(list(a))

a= [x for x in range(0,10,2)]

print(a)

b = list(map(lambda x:x*x,[1,2,3]))
print(b)


print(sorted([1,5,7,6,2,3,4],reverse = True))