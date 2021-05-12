a = [2, 4, 6, 1, -3, 9, -4, 3, 9, 4, 0, 1]

def max_triple(array):
	count = 0
	nums = None
	sum_nums = 0
	while (count <= len(array)-3):
		s = ([array[count], array[count+1], array[count+2]])
		if sum(s) > sum_nums:
			nums  = s
			sum_nums = sum(s)
		count += 1

	return nums

print(max_triple(a))
