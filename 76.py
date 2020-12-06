
import numpy as np

ways_list = [[-1 for i in range(0, 11)] for j in range(0, 11)]

def ways(n, k):
	#print("NUMBER: ", n)
	if n == 1 or n == 0:
		return 1
	way = 0
	k = n if k>n else k
	while k > 0:
		way += ways(n-k, k)
		k -= 1
	
	return way

print(np.matrix(ways_list))
print(ways(10, 9))



'''
1 -> /
2 -> 1 + 1
3 -> 2 + 1   -   1 + 1 + 1
4 -> 3 + 1   -   2 + 2    -        2 + 1 + 1         -         1 + 1 + 1 + 1  
'''

'''

3 + 1
2 + 2






'''