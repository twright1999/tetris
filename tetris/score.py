"""
score.py

class for manageing the score and level
"""

from utils import display
import pygame as pg

class Score:
	def __init__(self):
		self.level = 1
		self.score = 0

	def set_score(self, line_count):
		if line_count == 1:
			self.score += 100*self.level
		elif line_count == 2:
			self.score += 300*self.level
		elif line_count == 3:
			self.score += 500*self.level
		elif line_count == 4:
			self.score += 800*self.level

	def draw(self, screen):
		font = pg.font.Font('freesansbold.ttf',115)
		textsurface = font.render(str(self.score), False, (0, 0, 0))
		screen.blit(textsurface,(250,0))