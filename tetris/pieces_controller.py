"""
pieces_controller.py

class for controlling all pieces
"""

from . import piece
import math
import numpy as np
import pygame as pg

class PiecesController:

	def __init__(self, board):
		self.board = board
		self.current_piece = self.get_random_piece()
		self.hold_piece = None
		self.queue = [self.get_random_piece(),self.get_random_piece(),self.get_random_piece(),
					  self.get_random_piece(),self.get_random_piece()]

		self.piece_xpos = 3
		self.piece_ypos = 0
		self.BASE_VEL = 0.1
		self.piece_vel = self.BASE_VEL

	def input(self, keyboard_input):
		if keyboard_input[0] and keyboard_input[7]: # left
			self.check_boundary(-1)
			keyboard_input[7] = False
		if keyboard_input[1] and keyboard_input[8]: # right
			self.check_boundary(1)
			keyboard_input[8] = False
		if keyboard_input[2]: # down
			self.piece_vel = 0.3
		else:
			self.piece_vel = self.BASE_VEL
		if keyboard_input[3] and keyboard_input[9]: # space
			self.hard_drop()
			keyboard_input[9] = False
		if keyboard_input[4] and keyboard_input[10] and self.check_rotation(self.current_piece.get_acw()): # z
			self.current_piece.rotate_cw()
			keyboard_input[10] = False
		if keyboard_input[5] and keyboard_input[11] and self.check_rotation(self.current_piece.get_cw()): # x
			self.current_piece.rotate_acw()
			keyboard_input[11] = False
		if keyboard_input[6] and keyboard_input[12]: # c
			self.hold()
			keyboard_input[12] = False

		return (keyboard_input[7],keyboard_input[8],keyboard_input[9],keyboard_input[10],keyboard_input[11],keyboard_input[12])

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

		if np.count_nonzero(self.board.board) == np.count_nonzero(board):
			return True
		else:
			return False

	def check_boundary(self, direction):
		new_xpos = self.piece_xpos + direction
		board = self.get_new_board(self.current_piece.get_grid(), new_xpos, self.piece_ypos)

		if np.count_nonzero(self.board.board) == np.count_nonzero(board):
			self.piece_xpos = new_xpos

	def check_lock(self):
		new_ypos = self.piece_ypos + self.piece_vel
		board = self.get_new_board(self.current_piece.get_grid(), self.piece_xpos, new_ypos)

		if np.count_nonzero(self.board.board) == np.count_nonzero(board):
			self.piece_ypos = new_ypos
		else:
			self.board.board_before_piece_drop = self.board.board
			self.reset_piece()
			self.next_piece()

	def hard_drop(self):
		dropping = True
		new_ypos = self.piece_ypos
		prev_board = self.board.board
		while(dropping):
			new_ypos += 1
			board = self.get_new_board(self.current_piece.get_grid(), self.piece_xpos, new_ypos)

			if np.count_nonzero(self.board.board) != np.count_nonzero(board):
				dropping = False
				self.board.board_before_piece_drop = prev_board
				self.reset_piece()
				self.next_piece()

			prev_board = board

	def get_random_piece(self):
		random_number = np.random.randint(6)
		if random_number == 0:
			return piece.PieceI()
		elif random_number == 1:
			return piece.PieceT()
		elif random_number == 2:
			return piece.PieceO()
		elif random_number == 3:
			return piece.PieceL()
		elif random_number == 4:
			return piece.PieceJ()
		elif random_number == 5:
			return piece.PieceS()
		elif random_number == 6:
			return piece.PieceZ()

	def reset_piece(self):
		self.piece_xpos = 3
		self.piece_ypos = 0
		self.current_piece.current_rotation = 0

	def next_piece(self):
		self.current_piece = self.queue[0]

		for i in range(len(self.queue)-1):
			self.queue[i] = self.queue[i+1]

		self.queue[len(self.queue)-1] = self.get_random_piece()

	def hold(self):
		self.reset_piece()

		temp = self.hold_piece
		self.hold_piece = self.current_piece

		self.current_piece = temp if temp != None else self.get_random_piece()

	def draw(self, screen):
		self.draw_hold(screen)
		self.draw_queue(screen)

	def draw_hold(self, screen):
		if self.hold_piece != None:
			piece_grid = self.hold_piece.get_grid()

			for i in range(len(piece_grid)):
				for j in range(len(piece_grid[0])):
					if piece_grid[i][j] == 1:
						pg.draw.rect(screen, self.hold_piece.color,
							 (self.board.xpos+j*10,self.board.ypos-50+i*10,10,10))

	def draw_queue(self, screen):
		for p in range(len(self.queue)):
			piece_grid = self.queue[p].get_grid()

			for i in range(len(piece_grid)):
				for j in range(len(piece_grid[0])):
					if piece_grid[i][j] == 1:
						pg.draw.rect(screen, self.queue[p].color, 
							(10+(self.board.width*self.board.cell_size+j*10),self.board.ypos+(50*p+(i*10)),10,10))


	def update(self):
		self.check_lock()

	def set_board(self):
		return self.get_new_board(self.current_piece.get_grid(), self.piece_xpos, self.piece_ypos)

	def set_current_piece(self, piece):
		self.current_piece = piece
