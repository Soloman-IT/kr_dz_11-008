class Raspberry:
	states = {1:"первая стадия",
			  2:"вторая стадия",
			  3:"третья стадия"}
	def __init__(self, _index):
		self._index = _index
		self._state = Raspberry.states[1]

	def grow(self):
		if self._state == Raspberry.states[1]:

			self._state = Raspberry.states[2]
			return 1
		if self._state == Raspberry.states[2]:
			self._state = Raspberry.states[3]
			return 1

	def is_ripe(self):
		if self._state == Raspberry.states[3]:
			print("Созрела")
			return True
		else:
			print("Не созрела")
			return False

class RaspberryBush:
	raspberries = []
	def __init__(self, values):
		self.values = values
		for i in range(self.values):
			rasp = Raspberry(i)
			RaspberryBush.raspberries.append(rasp)

	def grow_all(self):
		for i in RaspberryBush.raspberries:
			i.grow()

	def all_are_ripe(self):
		return ([elem.is_ripe() for elem in RaspberryBush.raspberries])

	def give_away_all(self):
		RaspberryBush.raspberries.clear()

class Human:

	def __init__(self, name, _plant):
		self.name = name
		self._plant = _plant

	def work(self):
		self._plant.grow_all()

	def harvest(self):
		if  self._plant.all_are_ripe() == 1:
			print("Плоды созрели")
		else:
			print("Ран еще")
	@staticmethod
	def knowledge_base():
		print("""Сажают малину весной, осенью, зеленые черенки — летом.
		 		 Почву готовят заранее: при осенней посадке — где-то за месяц, при весенней — с осени.
		  		 Если не успели, то весной, где-то недели за 2-3, перед тем как соберетесь сажать.""")

ra = RaspberryBush(3)
garden_man = Human("Вадим", ra)
garden_man.work()
garden_man.harvest()
Human.knowledge_base()