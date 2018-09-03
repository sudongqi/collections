def partial_match(pattern):
	""" Calculate partial match table: String -> [Int]"""
	ret = [0]
	
	for i in range(1, len(pattern)):
		j = ret[i - 1]
		while j > 0 and pattern[j] != pattern[i]:
			j = ret[j - 1]
		ret.append(j + 1 if pattern[j] == pattern[i] else j)
	return ret
	
def kmp_search(T, P):
	""" 
	KMP search main algorithm: String -> String -> [Int] 
	Return all the matching position of pattern string P in S
	"""
	partial, ret, j = partial_match(P), [], 0
	
	for i in range(len(T)):
		while j > 0 and T[i] != P[j]:
			j = partial[j - 1]
		if T[i] == P[j]: j += 1
		if j == len(P): 
			ret.append(i - (j - 1))
			j = 0
		
	return ret
	
print(kmp_search('abbceabbdefg', 'abbde'))