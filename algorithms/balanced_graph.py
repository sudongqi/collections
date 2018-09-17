import collections

def balanced_graph(edges):
	"""
	Find minimum number of edges that can be added to the graph such that all nodes in the graph have 0 weighted degree
	O(2^2N)
	"""
	
	nodes = collections.defaultdict(int)
	for u, v, w in edges:
		nodes[u] -= w
		nodes[v] += w
		
	nodes = [val for val in nodes.values() if val!=0]
	if not nodes:
		return 0
	# print(account)
	
	dp = [len(nodes)] * (1 << len(nodes))
	# raise all combinations
	for i in range(1, len(dp)):
		balance = 0
		size = 0
		# get the total balance and size of this combination
		for j in range(len(nodes)):
			if 1<<j & i != 0:
				balance += nodes[j]
				size += 1
		# if the total balance is 0, then this is a subproblem
		if balance == 0:
			# minimum edges to achieve balance is size - 1
			dp[i] = size - 1
			# check all combination of i to get the optimal number of edges
			for j in range(1, i):
				if i & j == j and dp[j] + dp[i-j] < dp[i]:
					dp[i] = dp[j] + dp[i-j]
	
	return dp[-1]
	
test = [[0,1,10],[2,0,5]]
get = balanced_graph(test)
print(get)