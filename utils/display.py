"""
display.py

class for storing variables for displaying to the screen
"""

import pygame as pg

class Display:
	def __init__(self):
		self.line_count = 0

	def draw(self,screen):
		font = pg.font.Font('freesansbold.ttf',115)
		textsurface = font.render(str(self.line_count), False, (0, 0, 0))
		screen.blit(textsurface,(0,0))


