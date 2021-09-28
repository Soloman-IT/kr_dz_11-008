import random

class Warrior:
	def __init__(self, name ="No name", race = "Не указано", gender = "Не указано", scale = 0, buff_scale = 1):
		self.name = name
		self.max_hp = 100
		self.hp = 100
		self.race = race
		self.gender = gender
		self.buff_scale = buff_scale
		self.scale = scale  * self.buff_scale

	def Scale(self):
		if random.triangular(0.01,1) <= self.scale:
			return True
		return False



	def attack(self, enemy):
		if enemy.Scale() == True:
			print(enemy.race, enemy.class_say(), enemy.name, " уклонился от атаки ", self.race, self.class_say(), self.name)
			pass
		else:
			enemy.hp -= self.damage
			print( self.race, self.class_say(), self.name, " нанес удар ", enemy.race, enemy.class_say(), enemy.name)


	def bio(self):
		print("Раса : ", self.race)
		print("Пол : ", self.gender)
		print("Имя : ", self.name)
		print("HP : ", self.hp)


class Human(Warrior):
	def __init__(self, race = "Человек", buff_scale = 1.1):
		super().__init__()
		self.race = race
		self.buff_scale = buff_scale


class Light(Human):
	def __init__(self, scale = 0.3):
		super().__init__()
		self.scale = scale
		self.hp = 200
		self.damage = random.randint(30, 50)

	def class_say(self):
		return "Light"

class Heavy(Human):
	def __init__(self):
		super().__init__()
		self.hp = 500
		self.damage = random.randint(50, 70)

	def class_say(self):
		return "Heavy"

class Druid(Human):
	def __init__(self):
		super().__init__()
		self.hp = 100
		self.damage = 0
		self.scale = 0.7

	def class_say(self):
		return "Druid"

	def attack(self, enemy, friend):
		choice =  random.randint(0, 1)
		if choice == 1:
			if random.triangular(0.01, 1) <= 0.7:
				friend.hp = friend.max_hp
				print(self.race, self.class_say(), self.name, "вылечил", friend.race, friend.class_say(), friend.name)
			else :
				pass

		if choice == 0:
			if random.triangular(0.01, 1) <= 0.3:
				enemy.hp = 10
				print(self.race, self.class_say(), self.name, "понизил здоровье на 10  ", enemy.race, enemy.class_say(), enemy.name,)
			else:
				pass

class Orc(Warrior):
	def __init__(self, race = "Орк", buff_scale = 1.1):
		super().__init__()
		self.race = race
		self.buff_scale = buff_scale
		self.damage = 0
		self.damage = self.damage * self.buff_scale

class Berserk(Orc):
	def __init__(self):
		super().__init__()
		self.hp = 600
		self.max_hp = 600
		self.scale = 0.1
		self.damage = random.randint(60, 90)

	def class_say(self):
		return "Berserk"

class Shaman(Orc):
	def __init__(self):
		super().__init__()
		self.hp = 120
		self.max_hp = 120
		self.damage = 0

	def class_say(self):
		return "Shaman"

	def attack(self, enemy, friend):
		choice =  random.randint(0, 1)
		if choice == 1:
			if random.triangular(0.01, 1) <= 0.7:
				friend.hp = friend.max_hp
				print(self.race, self.class_say(), self.name, "вылечил", friend.race, friend.class_say(), friend.name)
			else :
				pass

		if choice == 0:
			if random.triangular(0.01, 1) <= 0.5:
				enemy.hp = 10
				print(self.race, self.class_say(), self.name, "понизил здоровье на 10  ", enemy.race, enemy.class_say(), enemy.name,)
			else:
				pass

def play():
	people_1 = []
	people_2 = []
	for i in range(2):
		heavy_chel = Heavy()
		heavy_chel.gender = "trap"
		heavy_chel.name = "(TEAM 1) Чел_жесткий_"+ str(i)
		people_1.append(heavy_chel)
	for i in range(2):
		heavy_chel = Berserk()
		heavy_chel.gender = "trap"
		heavy_chel.name = "(TEAM 2) Орк_жесткий_"+ str(i)
		people_2.append(heavy_chel)
	while True:
		print("Число 1 команды", len(people_1))
		print("Число 2 команды", len(people_2))
		while True:
			if len(people_1) == 0:
				print("Команда радикальных феминисток выиграла")
				exit()
			man_1 = random.choice(people_1)
			if man_1.hp <= 0:
				people_1.remove(man_1)
				continue
			else:
				break
		if man_1.class_say() == "Druid":
			while True:
				man_2 = random.choice(people_1)
				if man_1 != man_2:
					man_3 = random.choice(people_2)
					man_1.attack(man_3, man_2)
					break
				else:
					pass
		else:
			man_2 = random.choice(people_2)
			man_1.attack(man_2)

		while True:
			if len(people_2) == 0:
				print("Команда человеков выиграла")
				exit()
			man_1_2 = random.choice(people_2)

			if man_1_2.hp <= 0:
				people_2.remove(man_1_2)
			else:
				break

		if man_1_2.class_say() == "Druid":
			while True:
				man_2_2 = random.choice(people_2)
				if man_1_2 != man_2_2:
					man_3_2 = random.choice(people_1)
					man_1_2.attack(man_3_2, man_2_2)
					break
		else:
			man_2_2 = random.choice(people_1)
			man_1_2.attack(man_2_2)

play()