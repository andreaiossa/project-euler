'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

X = 600851475143
maxN = 1

def is_prime(x):
	k = 2
	while k < x:
		if x % k == 0:
			return False
		k += 1
	return True


def max_prime(x):
	k = 2
	global maxN
	while k <= x:
		if is_prime(k) and x % k == 0:
			maxN = k if k > maxN else maxN
			return max_prime(x/k)
		k += 1

max_prime(X)


print(maxN)