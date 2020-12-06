
import numpy as np

ways_list = [[-1 for i in range(0, 101)] for j in range(0, 101)]

def ways(n, k):
	global ways_list
	k = n if k > n else k
	
	if n <= 1:
		ways_list[n][k] = 1
		return 1
	
	if ways_list[n][k] != -1:
		return ways_list[n][k]

	way = 0
	q = 1
	while q <= k:
		way += ways(n-q, q)
		q += 1
		

	ways_list[n][k] = way
	return ways_list[n][k]
		
	

ways(100,99)
print(np.matrix(ways_list))
print(ways(100,99))



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