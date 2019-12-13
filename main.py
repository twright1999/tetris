"""
main.py

contains creates a game object and runs it
"""

from tetris import game

def main():
  	current_game = game.Game()
  	current_game.main()

if __name__=="__main__":
	main()