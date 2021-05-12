def split_pairs(string):
	data = []
	count = 0
	while count <= len(string):
		data.append(string[ count : count+2 ])
		count += 2
	data.pop()
	return data

print(split_pairs("acdc1233s"))