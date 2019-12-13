"""
game.py

contains main game loop
"""

import pygame as pg

from tetris import ball, board
from utils import controls

class Game:
	"""class which contains the main game loop"""
	def __init__(self):
		self.caption = "Tetris"
		self.screen_size = (800,500)
		self.screen = pg.display.set_mode(self.screen_size)
		self.clock = pg.time.Clock()
		self.done = False
		self.controls = controls.Controls()
		self.board = board.Board(self.screen_size[1])
		self.pieces = pieces.Pieces()

	def main(self):
		"""contains main game loop"""
		pg.init()
		pg.display.set_caption(self.caption)
		while not self.done:
			self.input()
			self.update()
			self.draw()
			self.clock.tick(120)
		pg.quit()

	def input(self):
		"""gets input from user and sets it to objects"""
		for event in pg.event.get():
			self.controls.check_keyboard_input(event)

			if event.type == pg.QUIT:
				self.done = True


	def update(self):
		"""update all objects"""
		self.ball.update()

	def draw(self):
		"""draw all objects"""
		self.screen.fill(pg.Color("white"))

		self.board.draw(self.screen)

		pg.display.flip()
