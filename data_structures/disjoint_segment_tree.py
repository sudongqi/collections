class Node(object):
	def __init__(self, start, end, k=1):
		self.k = k
		self.s = start
		self.e = end
		self.left = None
		self.right = None

class DisjointSegmentTree(object):
	def __init__(self):
		self.root = None
		self.k = 0

	def update(self, start, end):
		"""
		add interval [start, end) into the tree, return the maximum overlap in the tree
		"""
		self.root = self.insert(self.root, start, end, 1)
		return self.k
	
	def insert(self, root, start, end, k):
		if start >= end:
			return root
		if not root:
			self.k = max(self.k, k)
			return Node(start, end, k)
		else:
			if start >= root.e:
				root.right = self.insert(root.right, start, end, k)
				return root
			elif end <= root.s:
				root.left = self.insert(root.left, start, end, k)
				return root
			else:
				a = min(root.s, start)
				b = max(root.s, start)
				c = min(root.e, end)
				d = max(root.e, end)
				root.left = self.insert(root.left, a, b, root.k if root.s < start else k)
				root.right = self.insert(root.right, c, d, root.k if root.e > end else k)
				root.k += k
				root.s = b
				root.e = c
				self.k = max(root.k, self.k)
				return root


dst = DisjointSegmentTree()
print(dst.update(0, 10))
print(dst.update(15, 30))
print(dst.update(35, 50))
print(dst.update(9, 16))
print(dst.update(29, 35))
print(dst.update(0, 35))
# 1, 1, 1, 2, 2, 3
