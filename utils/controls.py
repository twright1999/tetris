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
		self.z = False
		self.x = False
		self.left_first = True
		self.right_first = True
		self.z_first = True
		self.x_first = True

	def get_input(self):
		"""return input as an array"""
		return [self.left,self.right,self.z,self.x, self.left_first, self.right_first, self.z_first, self.x_first]

	def set_first_press(self, first):
		self.left_first = first[0]
		self.right_first = first[1]
		self.z_first = first[2]
		self.x_first = first[3]

	def check_keyboard_input(self, event):
		"""checks input from the keyboard"""
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_LEFT:
				self.left = True
			if event.key == pg.K_RIGHT:
				self.right = True
			if event.key == pg.K_z:
				self.z = True
			if event.key == pg.K_x:
				self.x = True


		if event.type == pg.KEYUP:
			if event.key == pg.K_LEFT:
				self.left = False
				self.left_first = True
			if event.key == pg.K_RIGHT:
				self.right = False
				self.right_first = True
			if event.key == pg.K_z:
				self.z = False
				self.z_first = True
			if event.key == pg.K_x:
				self.x = False
				self.x_first = True