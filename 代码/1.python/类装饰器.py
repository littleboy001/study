class Test(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s"%func.__name__)
        self.__func = func
        func()
    def __call__(self):
        print("---装饰器中的功能---")
        self.__func()

@Test
def test():
	print("---test---")

test()

a = 1234
print(id(a))
b = 1234
print(id(b))
c = -2

#a = 124
#print(id(a))

print(id(c))