#定义一个4s店类
class Store(object):
	def order(self,money,size):
		return Select(money,size)


def Select(money,size):
	if money >=100000 and size == "索纳塔":
		return Suonata()
	elif money >=100000 and size == "名图":
		return Mingtu()	
	elif money >=100000 and size == "Ix35":
		return Ix35()	


#定义一个车类
class Car(object):
	def music(self):
		print("车正在放音乐")
	def drive(self):
		print("车正在行驶")
	def stop(self):
		print("车已经停好")

class Suonata(Car):
	pass
class Mingtu(Car):
	pass
class Ix35(Car):
	pass

#创建店的对象
car_store = Store()
car = car_store.order(200000,"索纳塔")
car.music()
car.drive()
car.stop()
