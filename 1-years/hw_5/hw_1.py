book = []
with open("Война_и_мир.txt", "r", encoding = "utf-8") as file:
	for row in file:
		book = file.readlines()

print(book[0])


russ_simv = "йцукенгшщзхъёфывапролджэячсмитьбюЮБЬТИМСЧЯЭЖДЛОРПАВЫФЪХЗЩШГНЕКУЦЙ"

def task_1(buka):
	for row in buka:
		if "Анна Павловна" in row:

			row = row.replace("Анна Павловна", "Anna Pavlovna")
			print(row)
def task_2(buka):
	for i in range(len(buka)):
		if buka[i].find("Princesse, ma parole") == -1:
			continue
		print(i) 

def task_3(buka):
	lst = []
	for i in buka:
		lst.append(i.split(" "))
	return lst

book = task_3(book)

def task_4(buka):
	count = 0
	for i in buka:
		for j in i:
			count += 1
	return count

def task_5(buka):
	for row in range(len(buka)):
		buka[row] = list(map(lambda el:el.lower(), buka[row]))

	return buka
book = task_5(book)

def del_func(buka):          #убрал все ["\n"]
	for i in (buka):
		if len(i) == 1:
			ind = book.index(i)
			book.pop(ind)
	return buka


book = del_func(book)

def debug_print(something):
	for i in range(10):
		print(something[i])

def func_for_6_task_1(row):
	rng = range(len(row))
	for i in rng:
		str_1 = ""
		for el in row[i]:
			if el in russ_simv:
				str_1 += el
		row[i] = str_1
	return row

def func_for_6_task_2(row):
	row_1 = []
	for i in range(len(row)):
		if row[i] != "":
			row_1.append(row[i])
	return row_1

def task_6(buka):
	buka = list(map(func_for_6_task_1,buka))
	buka = list(map(func_for_6_task_2,buka))
	return buka

book = task_6(book)

print(type(book))
def count_simv(row):
	simv = 0
	for i in range(len(row)):
		for j in range(len(row[i])):
			simv += 1
	# print(simv)
	return simv

def count_slov(row):
	return len(row)

def task_7(buka):
	sum_s = 0
	sum_r = 0
	print(type(map(count_slov, buka[0])))
	for i in range(len(buka)):
		sum_s += sum(list(map(count_simv, buka[i])))
		sum_r += len(buka[i])
	return sum_s/sum_r
task_7_da =  task_7(book)

def task_8(buka):
	sum_s = 0
	sum_r = 0
	for i in range(len(buka)):
		sum_s += sum(list(map(count_simv, buka[i])))
	return sum_s



def task_9(buka):
	lst = {}
	for i in buka:
 		for j in i:
 			if j not in lst.keys():
 				lst[j] = 0
 			else:
 				lst[j] = lst[j] +1
	list_keys = list(lst.items())
	list_keys.sort(key=lambda i: i[1])
	for i in range(1,11):
		print(list_keys[-i][0],list_keys[-i][1])
	
def task_10(buka):
	lst = {}
	for i in buka:
 		for j in i:
 			for k in j:

	 			if k not in lst.keys():
	 				lst[k] = 0
	 			else:
	 				lst[k] = lst[k] +1
	list_keys = list(lst.items())
	list_keys.sort(key=lambda i: i[1])
	for i in range(1,11):
		print(list_keys[-i][0],list_keys[-i][1])
task_10(book)
	
