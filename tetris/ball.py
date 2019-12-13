"""
ball.py

test class which creates a moveable ball
"""

import pygame as pg

class Ball:
	"""class for a simple user controlable ball"""
	def __init__(self, xp=100, yp=100, xv=2, yv=2, r=10):
		self.xpos = xp
		self.ypos = yp
		self.xvel = xv
		self.yvel = yv
		self.radius = r
		self.color = pg.Color("red")

		self.xdir = 0
		self.ydir = 0

	def input(self, keyboard_input):
		"""takes input and sets heading direction for the ball"""
		self.xdir = 0
		self.ydir = 0

		if keyboard_input[0]:
			self.xdir += -1
		if keyboard_input[1]:
			self.xdir += 1
		if keyboard_input[2]:
			self.ydir += -1
		if keyboard_input[3]:
			self.ydir += 1

		if not(keyboard_input[0] or keyboard_input[1]):
			self.xdir = 0
		if not(keyboard_input[2] or keyboard_input[3]):
			self.ydir = 0


	def update(self):
		"""update the position of the ball"""
		self.xpos += self.xvel*self.xdir
		self.ypos += self.yvel*self.ydir

	def draw(self, screen):
		"""draw the ball"""
		pg.draw.circle(screen, self.color, (self.xpos,self.ypos), self.radius)

