import pickle

dict_1 = {}
with open("freqrnc2011.csv", "r", encoding = "utf-8") as file:
	mywords = []
	file.readline()
	for row in file:
		a = row.strip().split("\t")
		# if (len(a[0]) in range(5,11)) and ("s" in a[1]):
		if a[1] == 's':
			mywords.append((a[0], float(a[2])))
			# dict_1[a[0]] = a[2]

# list_1 = list(dict_1.items())
mywords.sort(key = lambda i : i[1])
mywords.reverse()
mywords_1 = []
for i in range(15000):
	if len(mywords[i][0]) in range(5, 11):
		mywords_1.append(mywords[i])

str_1 = ""
for i in range(len(mywords_1)):
	str_1 += " " + mywords_1[i][0]

pickle.dump(str_1, open("da.pickle","wb"))

pickle.dump(str_1, open("da.pickle", "wb")) 
da = ""
pickle.load(da, open("da.pickle", "r"))
print(type(da))
