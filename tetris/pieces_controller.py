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
		self.piece_vel = 0.1

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

	def check_rotation(self, new_rotation):
		board = np.copy(self.board.board_before_piece_drop)
		piece_grid = self.current_piece.rotations[new_rotation]
		for i in range(len(piece_grid)):
			for j in range(len(piece_grid[0])):
				xpos = math.floor(self.piece_xpos+j)
				ypos = math.floor(self.piece_ypos+i)

				if 0 <= xpos < len(board[0]) and ypos < len(board):
					board[ypos,xpos] = self.current_piece.state if (
						piece_grid[i][j] == 1) else board[ypos,xpos]

		if np.count_nonzero(board) == 4:
			return True
		else:
			return False

	def check_move(self, direction):
		piece_grid = self.current_piece.get_grid()
		furthest_left_arr = np.full(4,len(piece_grid))
		furthest_right_arr = np.zeros(4)

		for i in range(len(piece_grid)):
			for j in range(len(piece_grid[0])):
				if piece_grid[i][j] == 1:
					if furthest_left_arr[i] == len(piece_grid):
						furthest_left_arr[i] = j
					furthest_right_arr[i] = j

		furthest_left = min(furthest_left_arr)
		furthest_right = max(furthest_right_arr)

		new_pos = self.piece_xpos + direction
		if (0-furthest_left) <= new_pos < (self.board.width-furthest_right):
			self.piece_xpos = new_pos	

	def update(self):
		# self.piece_ypos += self.piece_vel
		print

	def set_board(self):
		board = np.copy(self.board.board_before_piece_drop)
		piece_grid = self.current_piece.get_grid()
		for i in range(len(piece_grid)):
			for j in range(len(piece_grid[0])):
				xpos = math.floor(self.piece_xpos+j)
				ypos = math.floor(self.piece_ypos+i)

				if 0 <= xpos < len(board[0]) and ypos < len(board):
					board[ypos,xpos] = self.current_piece.state if (
						piece_grid[i][j] == 1) else board[ypos,xpos]

		return board

	def set_current_piece(self, piece):
		self.current_piece = piece
