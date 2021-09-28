mydict = {2:9, 5:-3, 3:3, 7:3, 4:20,
1:9, 6:9, 11:3, 13:6}

def f1(dc, n):
	rn = range(n)
	for k,(i, j) in zip(range(n) ,dc.items()):
		try:

			if k not in dc.keys() :
				dc[k] = "!!"
			dc[i] = k
		except:
			return dc
	return dc 
def f2(dc):
	lst = []
	for k, v in dc.items():
		lst.append(v)
	for k, v in dc.items():
		if v in lst:
			del dc[k]
		lst.append(v)
	return dc

k = 101

def f3(n):
	k = sum([int(el) for el in str(n)])
	print(k)
	while (k >= 10):
		n = sum([int(el) in n])
		k = sum([int(el) in n])
	return k
print(f3(156))

def f4(str_1):
	lst = ["у","е","ы","а","о","э","я","и"]
	lst_1 = []
	for i in range(len(str_1)):
		if str_1[i].lower() in lst:
			lst_1.append(str_1[i])
			lst_1.append("с")
		lst_1.append(str_1[i])
	str_2 = ""
	for i in range(len(lst_1)):
		str_2 += str(lst_1[i])

	return str_2
