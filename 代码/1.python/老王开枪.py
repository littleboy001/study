#创建类
class Person(object):
	"""人的类"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name#记录人的名字
		self.gun = None#记录老王手里的枪的信息
		self.hp = 100#记录人物血量
	def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
		"""把子弹装到弹夹中"""
		dan_jia_temp.baocun_zidan(zi_dan_temp)
	def anzhuang_danjia(self,gun_temp,dan_jia_temp):
		"""把弹夹安装到枪中"""
		gun_temp.baocun_danjia(dan_jia_temp)
	def naqiang(self,gun_temp):
		"""拿起枪"""
		self.gun = gun_temp#记录枪的引用
	def __str__(self):
		if self.gun:
			return "%s的血量为%d,他有枪,%s"%(self.name,self.hp,self.gun)
		else:
			if self.hp > 0:
				return "%s的血量为%d,他手里没抢"%(self.name,self.hp)
			else:
				return "敌人已挂。。。"
	def kou_ban_ji(self,enemy):
		"""让枪发射子弹打敌人"""
		#枪.开火(敌人)
		self.gun.fire(enemy)
	def diao_xue(self,sha_shang_li):
		"""敌人掉血,掉的血和子弹威力相当"""
		self.hp -= sha_shang_li
		

class Gun(object):
	"""枪类"""
	def __init__(self, name):
		super(Gun, self).__init__()
		self.name = name#记录枪的名字
		self.danjia = None#用来记录弹夹的引用
	def baocun_danjia(self,dan_jia_temp):
		"""用一个属性保存弹夹的引用"""
		self.danjia = dan_jia_temp
	def __str__(self):
		if self.danjia:
			return "枪的信息为%s,%s"%(self.name,self.danjia)
		else:
			return "枪的信息为%s,这把枪中没有弹夹"
	def fire(self,enemy):
		"""从弹夹中获取一颗子弹，用这颗子弹去打敌人"""
		#弹出一颗子弹
		zidan_temp = self.danjia.tanchu_zidan()
		#用这颗子弹去打中敌人
		if zidan_temp:
			zidan_temp.dazhong(enemy)
		else:
			print("子弹不足....")

class Danjia(object):
	"""弹夹类"""
	def __init__(self, max_num):
		super(Danjia, self).__init__()
		self.max_num = max_num#记录弹夹最大容量
		self.zidan_list = []#记录所有子弹的引用

	def baocun_zidan(self,zi_dan_temp):
		"""将这颗子弹保存"""
		self.zidan_list.append(zi_dan_temp)

	def __str__(self):
		return "弹夹的信息为%d/%d"%(len(self.zidan_list),self.max_num)
	def tanchu_zidan(self):
		"""弹出一颗子弹"""
		if self.zidan_list:
			return self.zidan_list.pop()
		else:
			return None


class Zidan(object):
	"""子弹类"""
	def __init__(self, sha_shang_li):
		super(Zidan, self).__init__()
		self.sha_shang_li = sha_shang_li#记录子弹的杀伤力
	def dazhong(self,enemy):
		"""子弹打中敌人,敌人掉血"""
		enemy.diao_xue(self.sha_shang_li)


def main():
	"""用来控制整个程序的流程"""
	#1.创建一个老王
	laowang = Person("老王")

	#2.创建一把枪
	ak47 = Gun("AK47")

	#3.创建一个弹夹
	dan_jia = Danjia(20)


	#4.创建一些子弹
	for i in range(20):
		
		zi_dan = Zidan(10)

	

		#5.老王把子弹装到弹夹里面
		#老王.安装子弹到弹夹中(弹夹,子弹)
		laowang.anzhuang_zidan(dan_jia,zi_dan)

	#6.老王把弹夹装到枪里面
	#老王.安装弹夹到枪中(枪,弹夹)
	laowang.anzhuang_danjia(ak47,dan_jia)
	"""
	#test测试弹夹的信息
	print(dan_jia)
	#test测试枪的信息
	print(ak47)
	"""
	#7.老王拿起枪
	#老王.拿枪(枪)
	laowang.naqiang(ak47)
	#test测试老王拿枪的信息
	print(laowang)
	#8.创建一个敌人
	gebi_laosong = Person("隔壁老宋")
	#print(gebi_laosong)
	#9.老王开枪打敌人
	#老王.扣扳机(隔壁老宋)
	for x in range(15):
		
		laowang.kou_ban_ji(gebi_laosong)
		print(laowang)
		print(gebi_laosong)





if __name__ == '__main__':
	main()

	