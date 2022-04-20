## Copyright Yapudpil pour RCorp™
from random import randint
import global_var as gv

class Manager:
	def __init__(self, game, rows, cols, diff):
		self.game = game
		self.rows = rows
		self.cols = cols

		diff_ref = {'Facile':1/8, 'Moyen':1/6, 'Difficile':1/5}
		self.bombs = round(self.rows * self.cols * diff_ref[diff])
		self.flags = self.bombs
		game.flags.set(self.flags)

		self.player_grid = [[-1 for c in range(self.cols)] for r in range(self.rows)]  # Fully undiscovered grid
		self.solution = [[0 for c in range(self.cols)] for r in range(self.rows)]  # Empty soluton
		self.fill_solution()

	def fill_solution(self):
		placed_bombs = 0
		while placed_bombs < self.bombs:
			r = randint(0, self.rows - 1)
			c = randint(0, self.cols - 1)
			if self.solution[r][c] != -3:
				self.solution[r][c] = -3
				placed_bombs += 1
				self.update_solution(r,c)

	def update_solution(self, r, c):
		#up
		if r-1 >= 0 and self.solution[r-1][c] != -3: self.solution[r-1][c] += 1
		#up left
		if r-1 >= 0 and c-1 >= 0 and self.solution[r-1][c-1] != -3: self.solution[r-1][c-1] += 1
		#left
		if c-1 >= 0 and self.solution[r][c-1] != -3: self.solution[r][c-1] += 1
		#down left
		if r+1 <= self.rows-1 and c-1 >= 0 and self.solution[r+1][c-1] != -3: self.solution[r+1][c-1]+=1
		#down
		if r+1 <= self.rows-1 and self.solution[r+1][c] != -3: self.solution[r+1][c] += 1
		#down right
		if r+1 <= self.rows-1 and c+1 <= self.cols-1 and self.solution[r+1][c+1] != -3: self.solution[r+1][c+1]+=1
		#right
		if c+1 <= self.cols-1 and self.solution[r][c+1] != -3: self.solution[r][c+1] += 1
		#up right
		if r-1 >= 0 and c+1 <= self.cols-1 and self.solution[r-1][c+1] != -3: self.solution[r-1][c+1] += 1

	def discover(self, r, c):
		self.game.error_msg.set('')  # Reset error message

		if self.player_grid[r][c] == -2:  # Flag
			self.game.error_msg.set('La case est marquée par un drapeau.')

		elif self.solution[r][c] == -3:  # Bomb
			gv.victory = False
			self.game.close_menu()
			return

		elif self.player_grid[r][c] == self.solution[r][c]:	# Square is already discovered -> do nothing
			return

		else:   # Normal square
			self.player_grid[r][c] = self.solution[r][c]
			self.game.display.update(self.solution[r][c], r, c)

			if self.solution[r][c] == 0:  # 0 is discovered -> discover squares around
				#up
				if r-1 >= 0:  self.discover(r-1, c)
				#up left
				if r-1 >= 0 and c-1 >= 0:  self.discover(r-1, c-1)
				#left
				if c-1 >= 0:  self.discover(r, c-1)
				#down left
				if r+1 <= self.rows-1 and c-1 >= 0:  self.discover(r+1, c-1)
				#down
				if r+1 <= self.rows-1:  self.discover(r+1, c)
				#down right
				if r+1 <= self.rows-1 and c+1 <= self.cols-1:  self.discover(r+1, c+1)
				#right
				if c+1 <= self.cols-1:  self.discover(r, c+1)
				#up right
				if r-1 >= 0 and c+1 <= self.cols-1:  self.discover(r-1, c+1)

	def flag(self, r, c):
		self.game.error_msg.set('')  # Reset error message

		if self.player_grid[r][c] == self.solution[r][c]:  # Already discovered square
			self.game.error_msg.set('La case est déjà découverte.')

		elif self.player_grid[r][c] == -2:  # Flag
			self.remove_flag(r, c)

		elif self.flags > 0:  # Normal square + remaining flags
			self.put_flag(r, c)

		else:  # No more flags
			self.game.error_msg.set('Tous les drapeaux ont été placés.')

	def put_flag(self, r, c):
		self.player_grid[r][c] = -2
		self.game.display.update(-2, r, c)

		self.flags -= 1
		self.game.flags.set(self.flags)

		if self.solution[r][c] == -3:  # If flag on bomb
			self.bombs -= 1
			if self.bombs == 0:
				gv.victory = True
				self.game.close_menu()

	def remove_flag(self, r, c):
		self.player_grid[r][c] = -1
		self.game.display.update(-1, r, c)

		self.flags += 1
		self.game.flags.set(self.flags)

		if self.solution[r][c] == -3:  # If flag on bomb
			self.bombs += 1