#-*- coding:utf-8 -*-
import pygame
import time
from pygame.locals import *
import random

class Base(object):
	def __init__(self,screen_temp,x,y,image_name):
		self.x = x
		self.y = y
		self.screen = screen_temp
		self.image = pygame.image.load(image_name)


class BasePlane(Base):
	def __init__(self,screen_temp,x,y,image_name):
		Base.__init__(self,screen_temp,x,y,image_name)
		self.buttle_list = []#存储发射出去的子弹的引用
	def display(self):
		self.screen.blit(self.iamge,(self.x,self.y))
		for bullet in self.buttle_list:
			bullet.display()
			bullet.move()
			if bullet.judge():#判断是否越界
				self.buttle_list.romove(bullet)

class BaseBullet(Base):
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

class HeroPlane(BasePlane):
	"""飞机类"""
	def __init__(self,screen_temp):
		BasePlane.__init__(self,screen_temp,210,700,"./feiji/hero1.png")
	
	def move_left(self):
		self.x -= 5	
	def move_left(self):
		self.x += 5	

	def fire(self):
		self.buttle_list.append(Bullet(self.screen,self.x,self.y))



class EnemyPlane(BasePlane):
	"""敌机类"""
	def __init__(self,screen_temp):
		BasePlane.__init__(self,screen_temp,0,0,"./feiji/enemy0.png")
		self.direction = "right"

	
	def move(self):
		if sefl.direction == "right":
			self.x += 5	
		elif sefl.direction == "left":
			self.x -= 5	
		
		if self.x > 430:
			sefl.direction = "left"
		elif self.x < 0:
			sefl.direction = "right"

	def fire(self):
		rand_num = random.randint(1,100) 
		if rand_num == 8 or rand_num ==10:
			self.buttle_list.append(EnemyBullet(self.screen,self.x,self.y))


class Buttle(BaseBullet):
	"""docstring for buttle"""
	def __init__(self, screen_temp,x,y):
		BaseBullet.__init__(self,screen_temp,x+40,y-20,"./feiji/buttle.png")
		
	def move(self):
		self.y -= 20
	
	def judge(self):
		if self.y < 200:
			return True
		else:
			return False

class EnemyButtle(BaseBullet):
	"""docstring for buttle"""
	def __init__(self, screen_temp,x,y):
		BaseBullet.__init__(self,screen_temp,x+25,y+40,"./feiji/buttle1.png")
	
	def move(self):
		self.y -= 20
	
	def judge(self):
		if self.y > 852:
			return True
		else:
			return False

def key_control(hero_temp):
	#判断是否是点击了退出按钮
    if event.type == QUIT:
        print("exit")
        exit()
    #判断是否是按下了键
    elif event.type == KEYDOWN:
        #检测按键是否是a或者left
        if event.key == K_a or event.key == K_LEFT:
            print('left')
            hero_temp.move_left()

        #检测按键是否是d或者right
        elif event.key == K_d or event.key == K_RIGHT:
            print('right')
            hero_temp.move_left()

        #检测按键是否是空格键
        elif event.key == K_SPACE:
            print('space')
            hero_temp.fire()

def main():
	#1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    #3创建一个飞机对象
    hero = HeroPlane(screen)

    #4.创建一个敌机
    enemy = EnemyPlane(screen)

    #4. 把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
		pygame.display.update()
		key_control(hero)

        time.sleep(0.01)


			


if __name__ == '__main__':
	main()