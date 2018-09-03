from heapq import heappush, heappop
from pprint import pprint


def astar_search(grid, src, des):
	"""
	f(x) = g(x) + h(x)
	g(x) is the current cost
	h(x) must underestimate the distance from x to tar
	"""
	
	h = lambda x: abs(des[0] - x[0]) + abs(des[1] - x[1])
	grid[src[0]][src[1]] = 2	
	q = [(0 + h(src), 0, src)]
	
	while q:
		est_cost, cost, node = heappop(q)
		if node == des:
			return cost
		for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			ci = node[0] + di
			cj = node[1] + dj
			if 0 <= ci < len(grid) and 0 <= cj < len(grid[0]) and grid[ci][cj]==0:
				heappush(q, (cost+1+h([ci, cj]), cost+1, [ci, cj]))
				grid[ci][cj] = 2
		print(q)
	return -1
	
grid = [
	[0,0,0,0,0,1,0,0,0],
	[1,1,0,1,0,1,0,1,0],
	[0,0,0,1,0,0,0,1,0],
	[0,1,0,1,1,1,0,0,0],
	[0,1,0,0,0,1,0,0,0],
	[0,1,0,1,0,1,0,0,0],
	[1,1,0,1,0,1,0,0,0],
	[0,0,0,1,0,0,0,0,0]
]

print(astar_search(grid, [7,0], [0,8]))
pprint(grid)