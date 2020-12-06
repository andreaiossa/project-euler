import math

length = int(math.pow(10, 4))+1

#divisors_matrix = [[0 for x in range(0, length)] for y in range(0, length )]
divisors_list = [[] for k in range(0, length)]


def divisors(n):
	if len(divisors_list[n]) == 0:
		print("DOING: ",  n)
		lista  = []
		k = n 
		while k > 1:
			if k == n:
				lista.append(k)
			elif n % k == 0:
				lista.append(k)
				if len(divisors_list[k]) != 0:
					lista += divisors_list[k]
				else:
					divisors(k)
					lista += divisors_list[k]

				
				if len(divisors_list[n/k]) != 0:
					lista += divisors_list[k]
				else:
					divisors(n/k)
					lista += divisors_list[k]
			k -= 1
		
		divisors_list[n] = list(set(lista))


N = int(math.pow(10, 4))

while N > 0:
	divisors(N)
	N -= 1


print(divisors_list[1264])