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
		self.down = False
		self.space = False
		self.z = False
		self.x = False
		self.c = False
		self.left_first = True
		self.right_first = True
		self.space_first = True
		self.z_first = True
		self.x_first = True
		self.c_first = True

	def get_input(self):
		"""return input as an array"""
		return [self.left,self.right,self.down,self.space,self.z,self.x,self.c, self.left_first,self.right_first,self.space_first,self.z_first,self.x_first,self.c_first]

	def set_first_press(self, first):
		self.left_first = first[0]
		self.right_first = first[1]
		self.space_first = first[2]
		self.z_first = first[3]
		self.x_first = first[4]
		self.c_first = first[5]

	def check_keyboard_input(self, event):
		"""checks input from the keyboard"""
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_LEFT:
				self.left = True
			if event.key == pg.K_RIGHT:
				self.right = True
			if event.key == pg.K_DOWN:
				self.down = True
			if event.key == pg.K_SPACE:
				self.space = True
			if event.key == pg.K_z:
				self.z = True
			if event.key == pg.K_x:
				self.x = True
			if event.key == pg.K_c:
				self.c = True

		if event.type == pg.KEYUP:
			if event.key == pg.K_LEFT:
				self.left = False
				self.left_first = True
			if event.key == pg.K_RIGHT:
				self.right = False
				self.right_first = True
			if event.key == pg.K_DOWN:
				self.down = False
			if event.key == pg.K_SPACE:
				self.space = False
				self.space_first = True
			if event.key == pg.K_z:
				self.z = False
				self.z_first = True
			if event.key == pg.K_x:
				self.x = False
				self.x_first = True
			if event.key == pg.K_c:
				self.c = False
				self.c_first = True

