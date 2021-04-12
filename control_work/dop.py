import random

class Player:

	def __init__(self, name):
		self.name = name
		self.scores = 0
		self.proverka = 0.8

	def hit(self, enemy, buff):
		num =  random.triangular(0.0001, 1)
		if num < self.proverka + buff:
			return True
		else:
			enemy.proverka -= buff
			return False

class Game:
	def __init__(self, pl_1, pl_2):
		self.pl_1 = pl_1
		self.pl_2 = pl_2

	def start_game(self):

		while (self.pl_1.scores < 11 and self.pl_2.scores < 11 ):
			for i in range(3):

				if self.pl_1.hit(self.pl_2, 0.05):
					self.pl_1.scores += 1

			for i in range(3):
				if self.pl_2.hit(self.pl_1, 0.05):
					self.pl_2.scores += 1
		if self.pl_1.scores == 11:
			print(self.pl_1.name)
		else:
			print(self.pl_2.name)
p1, p2 = Player("Ping"), Player("Pong")
game = Game(p1, p2)
game.start_game()