class SegmentTreeNode:
	def __init__(self, l, r, k):
		self.l, self.r = l, r
		self.k, self.lazy = k, 0
		self.left, self.right = None, None


class SegmentTree:
	def __init__(self, start, end):
		self.root = SegmentTreeNode(start, end, 0)
		
	def build(self, arr):
		# O(N)
		def dfs(i, j):
			node = SegmentTreeNode(i, j, None)
			if i==j:
				node.k = arr[i]
				return node
			m = i + (j - i) // 2
			node.left = dfs(i, m)
			node.right = dfs(m+1, j)
			node.k = max(node.left.k, node.right.k)
			return node
		self.root = dfs(0, len(arr)-1)
		

	def update(self, i, j, val):
		# O(log N)
		def dfs(node):
			self.normalize(node)
			# no overlap
			if i > j or node == None or i > node.r or j < node.l:
				return
			# total overlap: update lazy and propagate
			if i <= node.l and node.r <= j:
				node.lazy = val
				self.normalize(node)
				return
			# update children first and then self
			dfs(node.left)
			dfs(node.right)
			node.k = max(node.left.k, node.right.k)
		dfs(self.root)

	def query(self, i, j):
		# O(log N)
		def dfs(node):
			self.normalize(node)
			# no overlap
			if i > j or node == None or i > node.r or j < node.l:
				return -float('inf')
			# total overlap
			if i <= node.l and node.r <= j:
				return node.k
			# partial overlap
			return max(dfs(node.left), dfs(node.right))
		return dfs(self.root)

	def normalize(self, node):
		# update k using lazy value
		if node.lazy != 0: node.k += node.lazy
		if node.l < node.r:
			if not node.left:
				m = node.l + (node.r - node.l) // 2
				node.left = SegmentTreeNode(node.l, m, node.k)
				node.right = SegmentTreeNode(m + 1, node.r, node.k)
			# propagate to children
			elif node.lazy != 0:
				node.left.lazy += node.lazy
				node.right.lazy += node.lazy
		# reset lazy value
		node.lazy = 0


st = SegmentTree(0, 1000000)
st.build([3, 4, 5, 99, 2, 4, 7, 1])
print(st.query(0, 4))
print(st.query(4, 7))
st.update(4, 5, 100)
print(st.query(0, 7))
