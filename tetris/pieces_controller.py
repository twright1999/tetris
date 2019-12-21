"""
pieces_controller.py

class for controlling all pieces
"""

from .piece_classes import piece_i
import math
import numpy as np

class PiecesController():

	def __init__(self, board):
		self.board = board
		self.i = piece_i.PieceI()
		self.current_piece = self.i

		self.piece_xpos = 4
		self.piece_ypos = 4
		self.piece_vel = 0.01

	def input(self, keyboard_input):
		if keyboard_input[0] and keyboard_input[4]: # left
			self.check_move(-1)
			keyboard_input[4] = False
		if keyboard_input[1] and keyboard_input[5]: # right
			self.check_move(1)
			keyboard_input[5] = False
		if keyboard_input[2] and keyboard_input[6] and self.check_rotation(self.current_piece.get_acw()): # z
			self.current_piece.rotate_acw()
			keyboard_input[6] = False
		if keyboard_input[3] and keyboard_input[7] and self.check_rotation(self.current_piece.get_cw()): # x
			self.current_piece.rotate_cw()
			keyboard_input[7] = False

		return (keyboard_input[4],keyboard_input[5],keyboard_input[6],keyboard_input[7])

	def get_new_board(self, piece_grid, piece_xpos, piece_ypos):
		board = np.copy(self.board.board_before_piece_drop)
		for i in range(len(piece_grid)):
			for j in range(len(piece_grid[0])):
				xpos = math.floor(piece_xpos+j)
				ypos = math.floor(piece_ypos+i)

				if 0 <= xpos < len(board[0]) and ypos < len(board):
					board[ypos,xpos] = self.current_piece.state if (
						piece_grid[i][j] == 1) else board[ypos,xpos]

		return board

	def check_rotation(self, new_rotation):
		board = self.get_new_board(self.current_piece.rotations[new_rotation], self.piece_xpos, self.piece_ypos)

		if np.count_nonzero(board) == 4:
			return True
		else:
			return False

	def check_move(self, direction):
		new_xpos = self.piece_xpos + direction
		board = self.get_new_board(self.current_piece.get_grid(), new_xpos, self.piece_ypos)

		if np.count_nonzero(board) == 4:
			self.piece_xpos = new_xpos

	def update(self):
		self.piece_ypos += self.piece_vel

	def set_board(self):
		return self.get_new_board(self.current_piece.get_grid(), self.piece_xpos, self.piece_ypos)

	def set_current_piece(self, piece):
		self.current_piece = piece
