import random as rand, numpy as np

def generate(n, m, random = False):
	if random == False:
		return [[0 for i in range(m)] for i in range(n)]
	if random == True:
		return [[rand.randint(0,15) for i in range(m)] for i in range(n)]
	
mtr = generate(5, 5, True)

for i in mtr:
	print(i)
print()
def simple(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if 	i == j:
				matrix[i][j] = 1
			if i < j:
				matrix[i][j] = 2
			if i > j:
				matrix[i][j] = 0
	return matrix

def maximal(matrix, row = False, col = False):
	if row == True:
		count_max = 0
		row_1 = []
		for i in range(len(matrix)):
			count = 0
			for j in (matrix[i]):
				count += j
			if count > count_max:
				count_max = count

				row_1 = matrix[i]
		return row_1

	if col == True:
		count_max = 0
		row_1 = []
		for i in range(len(matrix)):
			count = 0
			for j in range(len(matrix)):
				count += matrix[j][i]
				row_1.append(matrix[j][i])
			if count > count_max:
				count_max = count
				row_2 = row_1[:]
			row_1 = []
		return (row_2)
	if col == False and row == False:
		val_max = matrix[0][0]
		for i in range(len(matrix)):
			count = 0
			for j in range(len(matrix)):
				if matrix[i][j] > val_max:
					val_max = matrix[i][j]
		return val_max

def sub(matrix,str_1, str_2, stolb_1, stolb_2):
	lst = []
	lst_1 = []
	for i in range(str_1, str_2+1):
		for j in range(stolb_1, stolb_2+1):
			lst.append(matrix[i][j])
		lst_1.append(lst)
		lst = []

	return lst_1
lst_1 = sub(mtr,1,4,1,3)



def rotate(matrix,str_1, str_2, stolb_1, stolb_2):
	if str_2 - str_1 == stolb_2 - stolb_1:
		lst = []
		lst_1 = []
		e = False
		print("!")
		a = range(str_1, str_2+1)
		b = range(stolb_1, stolb_2+1)
		count = 0
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				if i in a and j in b:
					e = True
					t = matrix[i][j]
					matrix[i][j] = matrix[j][i]
					matrix[j][i] = t
					print(t,"= t    ", matrix[i][j], " = elem ", matrix[j][i]," = tr elem")
				lst.append(matrix[i][j])
			lst_1.append(lst)
			lst = []
			count += 1
			if e == True:

				a = range(str_1 + count, str_2+1)
				b = range(stolb_1 + count, stolb_2+1)
			e = False
	return lst_1

m = rotate(mtr, 1, 4, 1, 4)

for i in m:
	print(i)
