"""
game.py

contains main game loop
"""

import pygame as pg


class Game:

	def __init__(self):
		self.caption = "Tetris"
		self.screen = pg.display.set_mode((800,400))
		self.clock = pg.time.Clock()
		self.done = False

	def main(self):
		pg.init()

		while not self.done:
			self.input()
			self.update()
			self.draw()

			self.clock.tick(60)

		pg.quit()

	def input(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.done = True

	def update(self):
		temp = "temp"

	def draw(self):
		self.screen.fill(pg.Color("red"))
		pg.display.flip()
