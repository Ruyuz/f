
class Node(object):
	def __init__(self, data, next_node = None):
		self.data = data
		self.next_node = next_node



class LinkedList(object):
	def __init__(self, head, length = 1):
		self.head = head
		self.length = length
	
	def insert(self, node, index = None):
		if self.head == None:#the linkedlist don't have a head
			self.head = node
			self.length = 1
		
		elif index == None:
			new_node = self.head
			while new_node.next_node != None:
				new_node = new_node.next_node
			new_node.next_node = node
			self.length += 1

		elif index == 0:
			node.next_node = self.head
			self.head = node
			
		else:
			new_node = self.head
			while index - 1 > 0:
				new_node = new_node.next_node
				index -= 1
			node.next_node = new_node.next_node
			new_node.next_node = node 
			self.length += 1

	def remove(self,index):
		if index >= self.length or self.head == None:
			return None
		elif index == 0:
			r = head
			self.head = self.head.next_node
			return r
		else:
			new_node = self.head
			while index - 1 > 0:
				new_node = new_node.next_node
				index -= 1
			r = new_node.next_node
			new_node.next_node = new_node.next_node.next_node
			self.length -= 1
			return r

	def find(self, data):
		new_node = self.head
		index = 0
		while new_node.next_node != None:
			if new_node.data == data:
				return index
			new_node = new_node.next_node
			index += 1
		if new_node.data == data:
			return index
		return None





