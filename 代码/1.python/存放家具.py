#定义一个房间类
class Room:
	def __init__(self,area,info,addr):
		self.area = area
		self.info = info
		self.addr = addr
		self.left_area = area
		self.contain_items = []

	def __str__(self):

		msg = "房子的总面积是：%d，剩余面积为：%d，类型是：%s，位置是：%s"%(self.area,self.left_area,self.info,self.addr)
		msg += ",当前房子里面的家具有%s"%(str(self.contain_items))
		return msg
	def add_item(self,item):
		self.left_area -= item.area
		self.contain_items = item.name

class Bed:
	def __init__(self,name,area):
		self.name = name
		self.area = area
	def __str__(self):
		return "床的面积是：%d，名字是：%s"%(self.area,self.name)

#定义一个家具类
home = Room(160,"三室一厅","北京")
print(home)



#创建房间对象
bed = Bed("席梦思",4)
print(bed)
home.add_item(bed)
print(home)
#创建家具对象
