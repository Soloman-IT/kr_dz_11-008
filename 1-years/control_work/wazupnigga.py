test = '''Wazzzzzuuuup bro haw ware youuuozw Zupppawazup ooo www zuuuppzup wupaz wupaz zoooo wzauuuuuppp ppppuz waz zaw upppzwaa uu zwa zwa'''

def func(str_1):
	list_1 = []
	print(str_1)
	if len(str_1) <= 5:
		return False
	list_2 = ["w","a","z","u","p"]
	proverka = True
	for elem in range(len(str_1)):
		print(str_1[elem])
		count = 0
		if str_1[elem].lower() not in list_1 and str_1[elem].lower() in list_2 :
			count += 1
			list_1.append(str_1[elem])
			print(list_1)
	print("count", count)
	if len(list_1) in range(4, 10):
		return str_1
list_1 = test.split(" ")
print(list_1)
text = list(filter(func, list_1))
print(text)