"""
score.py

class for manageing the score and level
"""

import pygame as pg
import math

class Score:
	def __init__(self,board):
		self.level = 1
		self.score = 0
		self.total_lines = 0
		self.board = board

	def set_score(self, line_count):
		if line_count != 0:
			self.total_lines += line_count
		if line_count == 1:
			self.score += 100*self.level
		elif line_count == 2:
			self.score += 300*self.level
		elif line_count == 3:
			self.score += 500*self.level
		elif line_count == 4:
			self.score += 800*self.level

	def update(self):
		self.level = 1+math.floor(self.total_lines/10)

	def draw(self, screen):
		font = pg.font.Font('freesansbold.ttf',30)

		string = "score: " + str(self.score)
		textsurface = font.render(string, False, (0, 0, 0))
		screen.blit(textsurface,(100+self.board.xpos+self.board.width*self.board.cell_size,self.board.ypos))

		string = "level: " + str(self.level)
		textsurface = font.render(string, False, (0, 0, 0))
		screen.blit(textsurface,(100+self.board.xpos+self.board.width*self.board.cell_size,100+self.board.ypos))

		string = "lines: " + str(self.total_lines)
		textsurface = font.render(string, False, (0, 0, 0))
		screen.blit(textsurface,(100+self.board.xpos+self.board.width*self.board.cell_size,200+self.board.ypos))