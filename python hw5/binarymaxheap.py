class Node(object):

	left_child = None
	right_child = None
	def __init__(self, key):
		self.key = key

class   BinaryMaxHeap(object):
	def __init__(self, root = None):
		self.root = root
		self.nums = [] # Define a list to store the key value of nodes in heap

	def heapify(self, *pos):
		for i in pos:
			self.nums.append(i)
		sorted_nums = sorted(self.nums, reverse = True)
		self.root = Node(sorted_nums[0])
		queue = [self.root]
		i = 1
		while i < len(sorted_nums):
			l = len(queue)
			while l:
				node = queue.pop(0)
				l = l - 1
				if i < len(sorted_nums):
					node_new = Node(sorted_nums[i])
					node.left_child = node_new
					i = i+1
					queue.append(node.left_child)
				if i < len(sorted_nums):
					node_new = Node(sorted_nums[i])
					node.right_child = node_new
					i = i+1
					queue.append(node.right_child)


	def push(self, node): # after call the heaplify function, self.nums will have all keys of heapnodes
		self.heapify(node.key)


	def delete(self, value):
		self.nums.remove(value)
		val = self.nums
		self.nums = []
		self.heapify(*val)
		return Node(value)


	def pop(self):
		value = self.root.key		
		sorted_nums = sorted(self.nums, reverse = True)
		sorted_nums.pop(0)
		self.nums = []
		self.heapify(*sorted_nums)
		return Node(value)

