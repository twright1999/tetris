"""
piece.py

parent class for pieces
"""

class Piece:

	def __init__(self):
		self.state = 1
		self.rotations = [[ [0,0,0,0],
							[1,1,1,1],
							[0,0,0,0],
						  	[0,0,0,0]],

						  [ [0,0,1,0],
						  	[0,0,1,0],
						  	[0,0,1,0],
						  	[0,0,1,0] ],

						  [ [0,0,0,0],
						  	[0,0,0,0],
						  	[1,1,1,1],
						  	[0,0,0,0] ],

						  [ [0,1,0,0],
						  	[0,1,0,0],
						  	[0,1,0,0],
						  	[0,1,0,0] ]]
		self.current_rotation = 0

	def get_cw(self):
		return (self.current_rotation+1)%4

	def get_acw(self):
		return (self.current_rotation-1)%4

	def rotate_cw(self):
		self.current_rotation = (self.current_rotation+1)%4

	def rotate_acw(self):
		self.current_rotation = (self.current_rotation-1)%4

	def get_grid(self):
		return self.rotations[self.current_rotation]

class PieceI(Piece):
	def __init__(self):
		super().__init__()
		self.state = 1
		self.rotations = [[ [0,0,0,0],
							[1,1,1,1],
							[0,0,0,0],
						  	[0,0,0,0]],

						  [ [0,1,0,0],
						  	[0,1,0,0],
						  	[0,1,0,0],
						  	[0,1,0,0] ],

						  [ [0,0,0,0],
						  	[0,0,0,0],
						  	[1,1,1,1],
						  	[0,0,0,0] ],

						  [ [0,0,1,0],
						  	[0,0,1,0],
						  	[0,0,1,0],
						  	[0,0,1,0] ]]

class PieceT(Piece):
	def __init__(self):
		super().__init__()
		self.state = 2
		self.rotations = [[ [0,1,0],
							[1,1,1],
						  	[0,0,0]],

						  [ [0,1,0],
						  	[1,1,0],
						  	[0,1,0] ],

						  [ [0,0,0],
						  	[1,1,1],
						  	[0,1,0] ],

						  [ [0,1,0],
						  	[0,1,1],
						  	[0,1,0] ]]

class PieceO(Piece):
	def __init__(self):
		super().__init__()
		self.state = 3
		self.rotations = [[ [1,1],
						  	[1,1]],

						  [ [1,1],
						  	[1,1] ],

						  [ [1,1],
						  	[1,1] ],

						  [ [1,1],
						  	[1,1] ]]

class PieceL(Piece):
	def __init__(self):
		super().__init__()
		self.state = 4
		self.rotations = [[ [0,0,1],
							[1,1,1],
						  	[0,0,0]],

						  [ [1,1,0],
						  	[0,1,0],
						  	[0,1,0] ],

						  [ [0,0,0],
						  	[1,1,1],
						  	[1,0,0] ],

						  [ [0,1,0],
						  	[0,1,0],
						  	[0,1,1] ]]

class PieceJ(Piece):
	def __init__(self):
		super().__init__()
		self.state = 5
		self.rotations = [[ [1,0,0],
							[1,1,1],
						  	[0,0,0]],

						  [ [0,1,0],
						  	[0,1,0],
						  	[1,1,0] ],

						  [ [0,0,0],
						  	[1,1,1],
						  	[0,0,1] ],

						  [ [0,1,1],
						  	[0,1,0],
						  	[0,1,0] ]]

class PieceS(Piece):
	def __init__(self):
		super().__init__()
		self.state = 6
		self.rotations = [[ [0,0,0],
							[0,1,1],
						  	[1,1,0]],

						  [ [0,1,0],
						  	[0,1,1],
						  	[0,0,1] ],

						  [ [0,0,0],
						  	[0,1,1],
						  	[1,1,0] ],

						  [ [0,1,0],
						  	[0,1,1],
						  	[0,0,1] ]]

class PieceZ(Piece):
	def __init__(self):
		super().__init__()
		self.state = 7
		self.rotations = [[ [0,0,0],
							[1,1,0],
						  	[0,1,1]],

						  [ [0,0,1],
						  	[0,1,1],
						  	[0,1,0] ],

						  [ [0,0,0],
						  	[1,1,0],
						  	[0,1,1] ],

						  [ [0,0,1],
						  	[0,1,1],
						  	[0,1,0] ]]