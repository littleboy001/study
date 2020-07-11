#-*- coding:utf-8 -*-
import pygame
import time
from pygame.locals import *
import random

class HeroPlane(object):
	"""飞机类"""
	def __init__(self,screen_temp):
		self.x = 210
		self.y = 700
		self.screen = screen_temp
		self.image = pygame.image.load("./feiji/hero1.png")
		self.buttle_list = []#存储发射出去的子弹的引用

	def display(self):
		self.screen.blit(self.iamge,(self.x,self.y))
		for bullet in self.buttle_list:
			bullet.display()
			bullet.move()
			if bullet.judge():#判断是否越界
				self.buttle_list.romove(bullet)
	
	def move_left(self):
		self.x -= 5	
	def move_left(self):
		self.x += 5	

	def fire(self):
		self.buttle_list.append(Bullet(self.screen,self.x,self.y))



class EnemyPlane(object):
	"""敌机类"""
	def __init__(self,screen_temp):
		self.x = 0
		self.y = 0
		self.screen = screen_temp
		self.image = pygame.image.load("./feiji/enemy0.png")
		self.buttle_list = []#存储发射出去的子弹的引用
		self.direction = "right"

	def display(self):
		self.screen.blit(self.iamge,(self.x,self.y))
		for bullet in self.buttle_list:
			bullet.display()
			bullet.move()
			if bullet.judge():#判断是否越界
				self.buttle_list.romove(bullet)
	
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


class Buttle(object):
	"""docstring for buttle"""
	def __init__(self, screen_temp,x,y):
		self.x = x+40
		self.y = y-20
		self.screen = screen_temp
		self.image = pygame.image.load("./feiji/buttle.png")
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
	def move(self):
		self.y -= 20
	
	def judge(self):
		if self.y < 200:
			return True
		else:
			return False

class EnemyButtle(object):
	"""docstring for buttle"""
	def __init__(self, screen_temp,x,y):
		self.x = x+25
		self.y = y+40
		self.screen = screen_temp
		self.image = pygame.image.load("./feiji/buttle1.png")
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
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