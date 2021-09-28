data = (line for line in open("dataset.csv", "r"))
print(next(data))
list_company = []
def check(data):
	all_raised = 0
	while (True):
		try:
			company_1 = next(data).split(";")
			if company_1[7].replace("\n", "").replace(",", "") == "a":
				all_raised += float(company_1[-2])
		except:
			break
	return all_raised
weight_raised = check(data)  / (30e6 - 10e6) * 1000
print(weight_raised)
data = (line for line in open("dataset.csv", "r"))
def generator_da(data, weight_raised):
	while(True):
		try:
			company_1 = next(data).split(";")
			if company_1[-1].replace("\n", "").replace(",", "") == "a" and float(company_1[-2]) < weight_raised :
				print(company_1)
				yield (company_1[0], company_1[2], company_1[-2])
		except:
			break
	return all_raised

da = generator_da(data, weight_raised)
count = 0
for i in da:
	count += 1
	print(da)
	print(count)