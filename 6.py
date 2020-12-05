'''
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
import math

result = 0
result2 = 0
for x in range(1, 101):
	result += math.pow(x, 2)

for k in range(1, 101):
	result2 += k

print(math.pow(result2, 2) - result)