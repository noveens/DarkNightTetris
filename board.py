import pygame, sys, os, time
from random import randint

from block import *

class board():
	def __init__(self, r, c):
		self.row = r
		self.col = c
		self.matrix = [[' ' for i in range(c) ] for j in range(r) ]
		self.screen = pygame.display.set_mode((20*int(c), 20*(r)+114))
		bg = pygame.image.load('ab.jpg')
		self.screen.fill((25,25,112))
		self.screen.blit(bg, (0,0))
		self.font = pygame.font.SysFont(None, 50)
		self.fonta = pygame.font.SysFont(None, 20)
		self.score = 0
		self.level = 0
		pygame.display.update() 

	def adda(self, x):
		self.score += x

	def bring_last(self):
		aa = []
		fl=0
		for c in range(self.col):
			aa.append(randint(0,1))
		for c in range(self.col):
			if self.matrix[0][c] == 'X' or self.matrix[0][c] == 'Y':
				fl=1
		if fl==0:
			for r in range(1,self.row,1):
				for c in range(self.col):
					self.update(r-1,c,self.matrix[r][c])
			for c in range(self.col):
				if aa[c] == 1:
					self.update(self.row-1, c, 'X')
				else:
					self.update(self.row-1, c, ' ')

	def reinit(self):
		bg = pygame.image.load('ab.jpg')
		self.screen.fill((25,25,112))
		self.screen.blit(bg, (0,0))

	def empty(self):
		for r in range(self.row):
			for c in range(self.col):
				self.update(r,c,' ')

	def bring_random(self):
		aa = []
		posr = []
		posc = []
		for i in range(self.level):
			x = block(randint(1,6))
			aa.append(x.tell())

		for i in range(self.level):
			posc.append(randint(3,29))
			posr.append(randint(10,25))

		x = 0
		l = posr[x]
		for i in aa:
			l = posr[x]
			for j in i:
				r = posc[x]
				for k in j:
					if k == 'Y': 
						self.update(l,r,'A')
					else: self.update(l,r,' ') 
					r+=1
				l+=1
			x+=1

	def next_level(self):
		if (self.level == 0 and self.score >= 0) or (self.level == 1 and self.score >= 100) or (self.level == 2 and self.score >= 500) or (self.level == 3 and self.score >= 1000) or (self.level == 4 and self.score >= 1500) or (self.level == 5 and self.score >= 2000):
			self.level += 1
			self.reinit()
			self.message('Welcome to Level: ', (255,0,0), 150, 275)
			self.message(str(self.level), (0,255,0), 470, 275)
			self.empty()
			self.bring_random()
			pygame.display.update()
			time.sleep(1)
			return 1
		return 0

	def message(self, msg, color, x, y):
		s = self.screen
		screentext = self.font.render(msg, True, color)
		s.blit(screentext, [x,y])
		pygame.display.update()

	def message2(self, msg):
		s = self.screen
		screentext = self.fonta.render(msg, True, (255,0,0))
		s.blit(screentext, [480,680])
		pygame.display.update()

	def show(self, msg, color):
		s = self.screen
		msg += str(self.score)
		screentext = self.font.render(msg, True, color)
		s.blit(screentext, [235,635])

	def check(self):
		for r in range(self.row-1, -1, -1):
			x = int(0)
			for c in range(self.col):
				if self.matrix[r][c] == 'X' or self.matrix[r][c] == 'A': 
					x+=1
			if x == self.col: 
				self.delete(r)
				self.adda(int(100))

	def delete(self, delete_row):
		for r in range(delete_row-1, -1, -1):
			for c in range(self.col):
				self.update(r+1,c,self.matrix[r][c])
				self.update(r,c,' ')

	def draw(self, x):
		self.screen.fill((25,25,112))
		bg = pygame.image.load('ab.jpg')
		self.screen.blit(bg, (0,0))

		count=0
		for r in range(self.row):
			for c in range(self.col):
				if self.matrix[r][c] == 'Y':
					count+=1
		if count==1:
			for r in range(self.row):
				for c in range(self.col):
					if self.matrix[r][c] == 'X':
						img = pygame.image.load('block.jpg')
						self.screen.blit(img, (20*int(c),20*int(r)))
					elif self.matrix[r][c] == 'A':
						img = pygame.image.load('gold.jpg')
						self.screen.blit(img, (20*int(c),20*int(r)))
					elif self.matrix[r][c] == 'Y' and x%3==0:
						img = pygame.image.load('block.jpg')
						self.screen.blit(img, (20*int(c),20*int(r)))

		else:
			for r in range(self.row):
				for c in range(self.col):
					if self.matrix[r][c] == 'X' or self.matrix[r][c] == 'Y':
						img = pygame.image.load('block.jpg')
						self.screen.blit(img, (20*int(c),20*int(r)))
					elif self.matrix[r][c] == 'A':
						img = pygame.image.load('gold.jpg')
						self.screen.blit(img, (20*int(c),20*int(r)))
		self.show('Score : ', (255,255,255) )
		self.message('Level : ', (255,0,0), 450, 30)
		self.message(str(self.level), (0,255,0), 570, 30)
		self.message2('To pause press <ESC>')
		pygame.display.update()

	def play(self):
		x = block(self.random())
		b = x.tell()

	def update(self,x,y,c):
		if x<self.row and x>=0 and y<self.col and y>=0:		
			self.matrix[x][y] = c

	def move_down(self):
		fl = 0
		count=0
		send=-1
		
		for r in range(self.row):
			for c in range(self.col):
				if self.matrix[r][c] == 'Y':
					count+=1
					if r+1 == self.row or self.matrix[r+1][c] == 'X' or self.matrix[r+1][c] == 'A':
						fl = 1
						send=r

		check = 100

		if fl==1 and count==1:
			self.adda(int(100))
			self.delete(send)

		if fl == 1:
			for r in range(self.row):
		 		for c in range(self.col):
		 			if self.matrix[r][c] == 'Y': 
		 				self.update(r,c,'X')
		 				check = min(check, r)
			if check == 0:
				bg = pygame.image.load('ab.jpg')
				self.screen.blit(bg, (0,0))
				return 2
			else:
				self.adda(int(10))	
				return 1

		else:
			for r in range(self.row-1,-1,-1):
				for c in range(self.col-1,-1,-1):
					if self.matrix[r][c] == 'Y':
						self.update(r+1,c,'Y')
						self.update(r,c,' ')
			return 0		

	def move_left(self):
		fl=0
		for r in range(self.row-1,-1,-1):
			for c in range(self.col):
				if self.matrix[r][c] == 'Y':
					if c-1<0 or self.matrix[r][c-1] == 'X' or self.matrix[r][c-1] == 'A': fl=1

		if fl==0:
			for r in range(self.row-1,-1,-1):
				for c in range(self.col):
					if self.matrix[r][c] == 'Y' and self.matrix[r][c-1] != 'X':
						self.update(r,c-1,'Y')
						self.update(r,c,' ')

	def move_right(self):
		fl=0
		for r in range(self.row-1,-1,-1):
			for c in range(self.col):
				if self.matrix[r][c] == 'Y':
					if c+1>=self.col or self.matrix[r][c+1] == 'X' or self.matrix[r][c+1] == 'A': fl=1

		if fl==0:
			for r in range(self.row-1,-1,-1):
				for c in range(self.col-1,-1,-1):
					if self.matrix[r][c] == 'Y' and self.matrix[r][c+1] != 'X':
						self.update(r,c+1,'Y')
						self.update(r,c,' ')

	def rotate(self, block, num):
		rot_block = list(reversed(zip(*block)))
		x,y = -1,-1
		for r in range(self.row):
		 	for c in range(self.col):
		 		if self.matrix[r][c] == 'Y':
		 			x = r
		 			y = c
		 		if x != -1 : 
		 			break
			if x != -1 :   
				break

		if block[0][0] == ' ': 
			y-=1

		i,j,fl = x,y,0

		rot = []
		for r in rot_block:
			l = []
		 	for c in r:
		 		l.append(c)
		 	rot.append(l)

		for r in rot_block:
		 	for c in r:
		 		if i>=self.row or i<0 or j<0 or j>=self.col or self.matrix[i][j] == 'X':
		 			fl=1
		 		j+=1
		 	if i>=self.row or i<0 or j<0 or j>=self.col or self.matrix[i][j] == 'X':
		 		fl=1
		 	i+=1
		 	j=y

		i,j = x,y

		if fl == 0:
			for r in range(self.row):
				for c in range(self.col):
					if self.matrix[r][c] == 'Y':
						self.update(r,c,' ')

			for r in rot_block:
		 		for c in r:
		 			self.update(i,j,c)
		 			j+=1
		 		i+=1
		 		j=y
			return rot

		else:
			return block