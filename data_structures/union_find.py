class UnionFind(object):
	def __init__(self):
		self.par = {}
		self.rnk = {}

	def __getitem__(self, x):
		if x not in self.par:
			self.par[x] = x
			self.rnk[x] = 0
		if self.par[x] != x:
			self.par[x] = self[self.par[x]]
		return self.par[x]

	def union(self, x, y):
		xr, yr = self[x], self[y]
		if self.rnk[xr] < self.rnk[yr]:
			self.par[xr] = yr
		elif self.rnk[xr] > self.rnk[yr]:
			self.par[yr] = xr
		else:
			self.par[yr] = xr
			self.rnk[xr] += 1
			

uf = UnionFind()
for i in range(10):
	uf[i]
uf.union(0, 9)
uf.union(1, 8)
uf.union(0, 1)
print (uf[7]==uf[9])
print (uf[8]==uf[9])
