from math import factorial


def k_combination(arr, _k):
	res = []
	stack = []
	
	def dfs(i, k):
		if k==0:
			res.append(stack[:])
			return
		if i >= len(arr):
			return
		# allow to skip if we have enough elements
		if len(arr) - i > k:
			dfs(i+1, k)
		stack.append(arr[i])
		dfs(i+1, k-1)
		stack.pop()
		
	dfs(0, _k)
	return res
	
	
n = 5
k = 3
vec = list(range(n))
get = k_combination(vec, k)

print(vec)
print(get)
print(len(get), factorial(n) // (factorial(k) * factorial(n-k)))
