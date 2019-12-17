"""
pieces_controller.py

class for controlling all pieces
"""

from .piece_classes import piece_i
import math
import numpy as np

class PiecesController():

	def __init__(self):
		self.i = piece_i.PieceI()
		self.current_piece = self.i

		self.piece_xpos = 4
		self.piece_ypos = 4
		self.piece_vel = 0.1

	def input(self, keyboard_input):
		if keyboard_input[0] and keyboard_input[4]: # left
			self.piece_xpos -= 1
			keyboard_input[4] = False
		if keyboard_input[1] and keyboard_input[5]: # right
			self.piece_xpos += 1
			keyboard_input[5] = False
		if keyboard_input[2] and keyboard_input[6]: # z
			self.current_piece.rotate_acw()
			keyboard_input[6] = False
		if keyboard_input[3] and keyboard_input[7]: # x
			self.current_piece.rotate_cw()
			keyboard_input[7] = False

		return (keyboard_input[4],keyboard_input[5],keyboard_input[6],keyboard_input[7])

	def update(self):
		self.piece_ypos += self.piece_vel

	def set_board(self, board):
		board = np.copy(board)
		piece_grid = self.current_piece.get_grid()
		for i in range(len(piece_grid)):
			for j in range(len(piece_grid[0])):
				xpos = math.floor(self.piece_xpos+j)
				ypos = math.floor(self.piece_ypos+i)

				if xpos < len(board[0]) and ypos < len(board):
					board[ypos,xpos] = self.current_piece.state if (
						piece_grid[i][j] == 1) else board[ypos,xpos]

		return board

	def set_current_piece(self, piece):
		self.current_piece = piece
