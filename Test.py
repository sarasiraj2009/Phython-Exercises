def four(arg1):
	list = arg1.split()
	print(list)
	x = []
	for i in list:
		y = list[i]
		print(y)
		for j in len(y):
			x[i] += int(y[j])
	
	return x

print(four("55 72 86"))