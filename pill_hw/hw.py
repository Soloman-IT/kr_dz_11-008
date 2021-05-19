mas = [[18, 7, 26, 42, 31],
	   [19, 38, 36, 52, 71],
	   [32, 48, 64, 56, 81],
	   [69, 58, 77, 12, 1]]

def blur_make(mas):
	def mean(numbers):
	    return float(sum(numbers)) / max(len(numbers), 1)
	    
	new_mas = []
	for i in range(len(mas)):
		list_3 = [] 
		for j in range(len(mas)):
			list_1 = [[i, j], [i, j-1], [i-1, j-1], [i-1, j], [i-1, j+1], [i, j+1], [i+1, j-1], [i+1, j+1], [i+1, j]]
			list_2 = []
			for elem in list_1:
				if elem[0] < 0 or elem[1] < 0:
					continue
				else:
					try:
						list_2.append(mas[elem[0]][elem[1]])
					except:
						pass
			print(list_2)
			list_3.append(mean(list_2))
		new_mas.append(list_3)
	return new_mas

print(blur_make(mas))