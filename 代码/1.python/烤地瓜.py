#定义一个地瓜类
class Sweetpotato:
	def __init__(self):
		self.cookedLevel = 0
		self.cookedString = "生的"
	def __str__(self):
		return("地瓜的状态是%s,烤的时间是%d"%(self.cookedString,self.cookedLevel))
	def cook(self,cooked_time):
		'''对地瓜进行烤'''
		self.cookedLevel += cooked_time
		if self.cookedLevel >= 0 and self.cookedLevel < 3:
			self.cookedString ="生的"
		if self.cookedLevel >= 3 and self.cookedLevel < 5:
			self.cookedString ="半生不熟"
		if self.cookedLevel >= 5 and self.cookedLevel < 8:
			self.cookedString ="熟的"
		if self.cookedLevel >= 8:
			self.cookedString ="糊的"
#创建一个地瓜对象
digua = Sweetpotato()
print(digua)
#调用地瓜的cook功能
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)