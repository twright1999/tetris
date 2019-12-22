"""
board.py

class for the game board
"""

import pygame as pg
import numpy as np
import math

class Board:
	"""class for the game board"""
	def __init__(self,sh):
		self.xpos = 0
		self.ypos = 50
		self.width = 10
		self.height = 20
		self.cell_size = math.floor((sh-self.ypos)/self.height)
		self.board = np.zeros((self.height,self.width))
		self.board_before_piece_drop = np.copy(self.board)

	def draw(self, screen):
		for i in range(self.height):
			for j in range(self.width):
				pg.draw.rect(screen, pg.Color("gray"), (self.xpos+(self.cell_size*j),
					self.ypos+(self.cell_size*i),self.cell_size,self.cell_size), 1)
				if self.board[i][j] == 1:
					pg.draw.rect(screen, pg.Color("cyan"), (self.xpos+(self.cell_size*j),
					self.ypos+(self.cell_size*i),self.cell_size,self.cell_size))
				if self.board[i][j] == 2:
					pg.draw.rect(screen, pg.Color("purple"), (self.xpos+(self.cell_size*j),
					self.ypos+(self.cell_size*i),self.cell_size,self.cell_size))
				if self.board[i][j] == 3:
					pg.draw.rect(screen, pg.Color("yellow"), (self.xpos+(self.cell_size*j),
					self.ypos+(self.cell_size*i),self.cell_size,self.cell_size))
				if self.board[i][j] == 4:
					pg.draw.rect(screen, pg.Color("orange"), (self.xpos+(self.cell_size*j),
					self.ypos+(self.cell_size*i),self.cell_size,self.cell_size))
				if self.board[i][j] == 5:
					pg.draw.rect(screen, pg.Color("blue"), (self.xpos+(self.cell_size*j),
					self.ypos+(self.cell_size*i),self.cell_size,self.cell_size))
				if self.board[i][j] == 6:
					pg.draw.rect(screen, pg.Color("green"), (self.xpos+(self.cell_size*j),
					self.ypos+(self.cell_size*i),self.cell_size,self.cell_size))
				if self.board[i][j] == 7:
					pg.draw.rect(screen, pg.Color("red"), (self.xpos+(self.cell_size*j),
					self.ypos+(self.cell_size*i),self.cell_size,self.cell_size))

	def check_line_break(self):
		line_break = False
		line_count = 0
		for i in range(self.height-1,0,-1):
			if np.count_nonzero(self.board_before_piece_drop[i]) == self.width:
				self.board_before_piece_drop[i] = 0
				line_break = True
				line_count += 1
			elif line_break:
				self.board_before_piece_drop[i+line_count] = self.board_before_piece_drop[i]

		if line_break:
			self.board_before_piece_drop[0:line_count] = 0

		return line_count




