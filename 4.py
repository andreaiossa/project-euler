'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

import numpy as np

start = 100
end = 999
maxN = 0
fact1 = 0
fact2 = 0

def is_palindro(string):
	max_index = len(string) -1
	for k in range(0, len(string)):
		if string[k] != string[max_index-k]:
			return False
	return True

matrix = [[0 for k in range(0, end-start)] for i in range(0, end-start)]

for x in range(0, end-start):
	for y in range(0, end-start):
		first = x + 100
		second = y +  100
		if matrix[x][y] == 0:
			result = first * second
			if is_palindro(str(result)) and result > maxN:
				maxN = result
				fact1 = first
				fact2 = second
			matrix[x][y] = matrix[y][x] = result

print(maxN, fact1, fact2)