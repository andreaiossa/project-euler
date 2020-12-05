

results = []

def indexes(string, n,  index, left, combination, result):
	if left == 0 or index >= len(string):
		if(len(combination) == n):
			result.append(combination)
	else:
		indexes(string, n, index +1, left-1, combination + [index], result)
		indexes(string, n, index +1, left, combination, result)
		
	
indexes("AB", 1, 0, 1, [], results)
print(results)

for x in range(1,1):
	print("ciao")