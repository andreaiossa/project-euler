'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

prime = {}

def is_prime(x):
	for key in prime:
		if x % prime[key] == 0:
			return False
	return True

counter = 0
result = 0
k=2

while True:
	if is_prime(k):
		if not str(k) in prime:
			prime[str(k)] = k
		print(k)
		counter += 1
		result = k
		if counter == 10001:
			break
	k += 1

print(result)

# 104743