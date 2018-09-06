import collections

class LFUCache(object):
	def __init__(self, capacity):
		self.remain = capacity
		self.nodesForFrequency = collections.defaultdict(collections.OrderedDict) # freq -> {key -> None}
		self.leastFrequency = 1 # pointer to the least frequent element
		self.nodeForKey = {} # key -> (value, freq)

	def _update(self, key, newValue=None):
		value, freq = self.nodeForKey[key]
		if newValue != None: 
			value = newValue
		self.nodesForFrequency[freq].pop(key)
		if len(self.nodesForFrequency[self.leastFrequency]) == 0: 
			self.leastFrequency += 1
		self.nodesForFrequency[freq+1][key] = None
		self.nodeForKey[key] = (value, freq+1)

	def get(self, key):
		if key not in self.nodeForKey: 
			return -1
		self._update(key)
		return self.nodeForKey[key][0]

	def put(self, key, value):
		if key in self.nodeForKey: 
			self._update(key, value)
		else:
			self.nodeForKey[key] = (value, 1)
			self.nodesForFrequency[1][key] = None
			if self.remain == 0:
				removed = self.nodesForFrequency[self.leastFrequency].popitem(last=False)
				self.nodeForKey.pop(removed[0])
			else: 
				self.remain -= 1
			self.leastFrequency = 1 # should be one after adding a new item
			
cache = LFUCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.get(1)
cache.get(1)
cache.put(4, 4)
cache.put(5, 5)
print([cache.get(i) for i in range(1, 6)])
