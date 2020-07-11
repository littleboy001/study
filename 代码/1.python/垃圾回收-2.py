a = "abcd"

print(id(a))
b = "abcd"
print(id(b))

del(a)
del(b)
c = "abcd"
print(id(c))
