"""
piece_i.py

class for i piece
"""

import pygame as pg

class PieceI:

	def __init__(self):
		self.state = 1
		self.rotations = [[ [0,0,0,0],
							[1,1,1,1],
							[0,0,0,0],
						  	[0,0,0,0]],

						  [ [0,0,1,0],
						  	[0,0,1,0],
						  	[0,0,1,0],
						  	[0,0,1,0] ],

						  [ [0,0,0,0],
						  	[0,0,0,0],
						  	[1,1,1,1],
						  	[0,0,0,0] ],

						  [ [0,1,0,0],
						  	[0,1,0,0],
						  	[0,1,0,0],
						  	[0,1,0,0] ]]
		self.current_rotation = 0

	def rotate_cw(self):
		self.current_rotation = (self.current_rotation+1)%4

	def rotate_acw(self):
		self.current_rotation = (self.current_rotation-1)%4

	def get_grid(self):
		return self.rotations[self.current_rotation]