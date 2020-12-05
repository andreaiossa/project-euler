'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''

prime = {}
comb_matrix = [[0 for x in range(0,100)] for y in range(0,100)]

def is_prime(x):
	if str(x) in prime:
		return True
	for key in prime:
		if x % prime[key] == 0:
			return False
	return True

def is_prime2(x):
	if str(x) in prime:
		return True
	k = 2
	while k < x:
		if x % k == 0:
			return False
		k += 1
	return True

def indexes(string, n,  index, left, combination, result):
	if n == 0:
		return []
	if left == 0 or index >= len(string):
		if(len(combination) == n):
			result.append(combination)
	else:
		indexes(string, n, index +1, left-1, combination + [index],result)
		indexes(string, n, index +1, left, combination,result)

def run(comb, xString):
	family = 0
	minim = None
	failure = 0
	for i in range(0, 10):
		if failure > 2:
			return False
		placeholder = list(xString)
		N = None
		for n in comb:
			if i == 0:
				if int(n) == 0:
					break 
			placeholder[int(n)] = str(i)
			N = int(''.join(placeholder))
		if N and is_prime2(N):
			
			family += 1
			if not minim or N < minim:
				minim = N
		else:
			failure += 1
			
		if family == 8:	
			return minim
	


def combination(x):
	print("TENTATIVO: ", x)
	xString = str(x)
	length = len(xString) - 1
	result = None

	for n in range(1, length + 1):
		combinations = []
		if comb_matrix[len(xString)][n]:
			combinations = comb_matrix[len(xString)][n]
		else:
			indexes(xString, n, 0, n, [], combinations)
			comb_matrix[len(xString)][n] = combinations

		for comb in combinations:
			value = run(comb, xString)
			if value:
				if not result or value < result:
					result = value

		
	print("RESULT: ", result)
	return result








k = 2
result = None
while True:
	if is_prime(k):
		if not str(k) in prime:
			prime[str(k)] = k
		result = combination(k)
		if result:
			break
	k += 1

print(result)