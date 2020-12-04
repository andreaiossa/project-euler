'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import math 

dictio = {}
result = 1

def is_prime(x):
	k = 2
	while k < x:
		if x % k == 0:
			return False
		k += 1
	return True

def scomposition(x, d):
	k = 2
	while k <= x and k!= 1:
		if is_prime(k) and x % k == 0:
			d[str(k)] = d[str(k)] + 1 if str(k) in d else 1
			return scomposition(x/k, d)
		k += 1
	return d

for x in range(2, 20):
	dicto = scomposition(x, {})
	for k in dicto:
		if k in dictio:
			dictio[k] = dicto[k] if dicto[k] > dictio[k] else dictio[k]
		else:
			dictio[k] = dicto[k]

for key in dictio:
	result *= math.pow(int(key), dictio[key])

print(result)