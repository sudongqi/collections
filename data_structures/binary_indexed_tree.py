class BinaryIndexedTree(object):
	def __init__(self, n):
		self.sums = [0] * (n + 1)

	def update(self, i, val):
		i += 1
		while i < len(self.sums):
			self.sums[i] += val
			# find next
			i += i & -i

	def sum(self, i):
		res = 0
		while i > 0:
			res += self.sums[i]
			# find parents
			i -= i & -i
		return res
		
bit = BinaryIndexedTree(10)
bit.update(3, 5)
bit.update(6, 5)
print(bit.sum(7))