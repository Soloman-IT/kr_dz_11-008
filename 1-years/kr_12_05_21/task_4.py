a = {1:2, 3:4}
b = {1:10, 2:5, 7:10}
c = {1:7, 2:10}

def merge(*args):
	all_dict = {}

	for i in args:
		print(i, "словарь")
		for k, v in i.items():
			print(k, v, "значения")
			if k in all_dict.keys():

				all_dict[k].append(v)
				print(all_dict[k])
				continue
			all_dict[k] = [v]

	for k, v in all_dict.items():
		if len(v) == 1:
			all_dict[k] = v[0]

	return all_dict

print(merge(a, b, c))