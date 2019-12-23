"""
game.py

contains main game loop
"""

import pygame as pg

from tetris import ball, board, pieces_controller, score
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
		self.pieces_controller = pieces_controller.PiecesController(self.board)
		self.score = score.Score(self.board)

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

		keyboard_input = self.controls.get_input()
		self.controls.set_first_press(self.pieces_controller.input(keyboard_input))

	def update(self):
		"""update all objects"""
		self.board.board = self.pieces_controller.set_board()
		self.pieces_controller.update()
		self.score.set_score(self.board.check_line_break())

	def draw(self):
		"""draw all objects"""
		self.screen.fill(pg.Color("white"))
		self.board.draw(self.screen)
		self.score.draw(self.screen)
		self.pieces_controller.draw(self.screen)

		pg.display.flip()
