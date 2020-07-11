import types
class P(object):
	def __init__(self,name):
		self.name = name
def eat(self):
	print("---%s正在吃---"%self.name)
p1 = P("laowang")
#p1.eat =types.MethodType(eat,p1)
#p1.eat()
p1.eat = eat
p1.eat(p1)
