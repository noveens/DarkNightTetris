import pygame, sys, os, time
from random import randint


class block():
	def __init__(self, r):
		self.r = r

	def tell(self):
		if self.r >= 8:
			self.r = (self.r % 7) + 1
		if self.r == 1:
			return [['Y'] * 4]
		elif self.r == 2:
			return [['Y','Y'],['Y','Y']]
		elif self.r == 3:
			return [[' ', 'Y', ' '],['Y','Y','Y']]
		elif self.r == 4:
			return [['Y','Y',' '],[' ','Y','Y']]
		elif self.r == 5:
			return [[' ','Y','Y'],['Y','Y',' ']]
		elif self.r == 6:
			return [['Y','Y','Y'],[' ',' ','Y']]
		elif self.r == 7:
			return [['Y']]