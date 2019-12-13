"""
game.py

contains main game loop
"""

import pygame as pg

from tetris import ball
from utils import controls

class Game:

	def __init__(self):
		self.caption = "Tetris"
		self.screen = pg.display.set_mode((800,400))
		self.clock = pg.time.Clock()
		self.done = False
		self.controls = controls.Controls()
		self.ball = ball.Ball()

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
			self.controls.check_user_input(event)

			if event.type == pg.QUIT:
				self.done = True

		self.ball.input(self.controls.get_input())

	def update(self):
		self.ball.update()

	def draw(self):
		self.screen.fill(pg.Color("white"))

		self.ball.draw(self.screen)

		pg.display.flip()
