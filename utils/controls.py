"""
controls.py

class for user inputs
"""

import pygame as pg

class Controls:
	"""class which contains booleans for the keyboard input"""
	def __init__(self):
		self.left = False
		self.right = False
		self.up = False
		self.down = False 

	def get_input(self):
		"""return input as an array"""
		return [self.left,self.right,self.up,self.down]

	def check_keyboard_input(self, event):
		"""checks input from the keyboard"""
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_a:
				self.left = True
			if event.key == pg.K_d:
				self.right = True
			if event.key == pg.K_w:
				self.up = True
			if event.key == pg.K_s:
				self.down = True
		if event.type == pg.KEYUP:
			if event.key == pg.K_a:
				self.left = False
			if event.key == pg.K_d:
				self.right = False
			if event.key == pg.K_w:
				self.up = False
			if event.key == pg.K_s:
				self.down = False