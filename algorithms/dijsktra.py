import collections
from heapq import *


def dijsktra(edges, source, target):
	
	graph = collections.defaultdict(list)
	for a, b, cost in edges:
		graph[a].append((b, cost))
		graph[b].append((a, cost))
	
	q = [(source, 0)]
	dist = {source: 0}
	prev = {source: source}
	
	while q:
		curr, cost = heappop(q)
		for nei, add_cost in graph[curr]:
			new_cost = cost + add_cost
			if new_cost < dist.get(nei, float('inf')):
				heappush(q, (nei, new_cost))
				dist[nei] = new_cost
				prev[nei] = curr
				
	path = [target]
	while prev[path[-1]] != path[-1]:
		path.append(prev[path[-1]])
	return dist[target], path[::-1]
	
	
edges = [[0, 1, 4], [1, 2, 8], [2, 3, 7], [3, 4, 9], [4, 5, 10], [3, 5, 14], [2, 5, 4], 
[5, 6, 2], [2, 8, 2], [8, 6, 6], [6, 7, 1], [7, 8, 7], [1, 7, 11], [0, 7, 8]]
res = dijsktra(edges, 0, 4)
print(res)
