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
		self.left_first = True
		self.right_first = True

	def get_input(self):
		"""return input as an array"""
		return [self.left,self.right,self.up,self.down, self.left_first, self.right_first]

	def set_first_press(self,first):
		self.left_first = first[0]
		self.right_first = first[1]

	def check_keyboard_input(self, event):
		"""checks input from the keyboard"""
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_a:
				self.left = True
			if event.key == pg.K_d:
				self.right = True

		if event.type == pg.KEYUP:
			if event.key == pg.K_a:
				self.left = False
				self.left_first = True
			if event.key == pg.K_d:
				self.right = False
				self.right_first = True