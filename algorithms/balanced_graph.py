import collections
import itertools

def balanced_account(transactions):
	"""
	same problem as balanced_graph below, a very fast greedy solution
	"""
	
	balances = collections.defaultdict(int)
	for giver, receiver, amount in transactions:
		balances[giver] -= amount
		balances[receiver] += amount
	balance = {person: balance for person, balance in balances.items() if balance!=0}
	people = {person for person in balance} 

	def dfs(people):
		if not people:
			return 0
		people_list = list(people)
		# starting with small combination k=2
		for i in range(2, len(people)+1):
			for selected in itertools.combinations(people_list, i):
				# if this combination has total balance equal to 0, we will proceed with this combination
				if sum(balances[p] for p in selected) == 0:
					return dfs(people-set(selected)) + len(selected) - 1
	return dfs(people)

def balanced_graph(edges):
	"""
	Find minimum number of edges that can be added to the graph such that all nodes in the graph have 0 weighted degree
	O(2^2N) bitarray solution
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
	
test = [[0,1,10],[2,0,5],[2,3,7],[3,1,2],[3,4,7]]
get = balanced_graph(test)
get2 = balanced_account(test)
print(get, get2)