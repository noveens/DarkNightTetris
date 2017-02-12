import pygame, sys, os, time
from random import randint

from board import *
from block import *

class gameplay(board):
	def __init__(self, r, c):
		self.score = int(0)
		self.rows = int(r)
		self.col = int(c)
		self.game = board(int(r),int(c))
		self.score = int(0)
		self.FPS = int(12)
		self.level = 0

	def random(self):
		return randint(1,15)

	def tella(self):
		x = self.score
		return x

	def up(self, x):
		self.FPS += x

	def inst(self):
		self.game.reinit()
		self.game.message('To move left press <a> or <LEFT>', (255,255,255), 20, 30)
		self.game.message('To move right press <d> or <RIGHT>', (255,255,255), 20, 130)
		self.game.message('To rotate press <s>', (255,255,255), 20, 230)
		self.game.message('To speed up game press <UP>', (255,255,255), 20, 330)
		self.game.message('To speed down game press <DOWN>', (255,255,255), 20, 430)
		self.game.message('To go back press <ESC>', (255,255,255), 20, 530)

		ret = 1

		s = 1
		while s:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					ret = 0
					s = 0
				if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE):
					s = 0

		return ret

	def play(self):

		ret, x = 1, 0
		self.game.reinit()
		self.game.message('To start press <SPACE_BAR>', (255,255,255), 70, 100)
		self.game.message('To quit press <q> or <ESC>', (255,255,255), 70, 200)
		self.game.message('To start from level other than 1,', (255,255,255), 70, 300)
		self.game.message('enter any number b/w 1 and 5', (255,255,255), 73, 335)
		self.game.message('For instructions press <i>', (255,255,255), 73, 435)

		s = 1
		while s:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					ret = 0
					s = 0
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					s = 0
				if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q):
					s = 0
					ret = 0
				if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
					ret = self.inst()
					self.game.reinit()
					self.game.message('To start press <SPACE_BAR>', (255,255,255), 70, 100)
					self.game.message('To quit press <q> or <ESC>', (255,255,255), 70, 200)
					self.game.message('To start from level other than 1,', (255,255,255), 70, 300)
					self.game.message('enter any number b/w 1 and 5', (255,255,255), 73, 335)
					self.game.message('For instructions press <i>', (255,255,255), 73, 435)
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					s = 0

		t = pygame.time.Clock()

		fl = 0
		som = 0

		left,right = 0,0
		pause = 0

		if ret: self.game.next_level()

		while ret:
			if fl == 0:
				num = self.random()
				s = block(num)
				bl = s.tell()
				count=13
				count2=-1
				for i in bl:
					count2 += 1
					for j in i:
						count += 1
						if j == 'Y' : self.game.update(count2,count,'Y')
						if j == ' ' : self.game.update(count2,count,' ')
					count=13
				fl=1

			if fl == 1:
				m = self.game.move_down()

			if m == 1:
				fl=0

			if m == 2: 
				ret=0

			if left==0 and right==0:
				for event in pygame.event.get():
					
					if event.type == pygame.QUIT: 
						ret = 0

					if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
						pause = 1
						self.game.reinit()
						self.game.message('You have paused the game', (255,0,0), 100, 250)
						self.game.message('To resume press <SPACE_BAR>', (0,255,0), 55, 350)
						while pause:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									ret = 0
									pause = 0
								if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE):
									pause = 0
					
					if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
						self.game.move_right()
						right=1
					
					if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
						self.game.move_left()
						left=1
					
					if event.type == pygame.KEYDOWN and (event.key == pygame.K_s):
						bl = self.game.rotate(bl, num)

					if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN):
						self.FPS += 2
						self.FPS = min(self.FPS, 18)

					if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP):
						self.FPS -= 2
						self.FPS = max(self.FPS, 6)

					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						r=0
						z=0
						while r==0 and z<=1000: 
							r = self.game.move_down()
							z+=1

						fl=0
						if r==2: ret=0

			elif left==1:
				for event in pygame.event.get():
					if event.type == pygame.QUIT: 
						ret = 0
					if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
						left = 0
					if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
						bl = self.game.rotate(bl, num)
					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						r=0
						z=0
						left=0
						while r==0 and z<=1000: 
							r = self.game.move_down()
							z+=1

						fl=0
						if r==2: ret=0
				if left==1: self.game.move_left()

			elif right==1:
				for event in pygame.event.get():
					if event.type == pygame.QUIT: 
						ret = 0
					if event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
						right = 0
					if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
						bl = self.game.rotate(bl, num)
					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						r=0
						z=0
						right=0
						while r==0 and z<=1000: 
							r = self.game.move_down()
							z+=1

						fl=0
						if r==2: ret=0
				if right==1: self.game.move_right()

			self.game.check()

			if self.level >= 1 and som%300 == 0:
				self.game.bring_last()

			if ret:  self.game.draw(som)
			som += 1
			t.tick(self.FPS)

			aaa = self.game.next_level()
			if aaa: 
				self.up(5)
				self.level += 1

		self.game.reinit()
		self.game.show('Score : ', (255,255,255) )
		self.game.message("Well Tried !", (255,255,255), 225, 280)
		time.sleep(1)

pygame.init()
game = gameplay(int(30),int(32))
game.play()