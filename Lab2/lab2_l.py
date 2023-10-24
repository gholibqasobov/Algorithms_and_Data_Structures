# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.next = None
#
#
# class LinkedList:
# 	def __init__(self, head=None):
# 		self.head = head
#
# 	def append(self, data):
# 		new_node = Node(data)
# 		current = self.head
#
# 		if current:
# 			while current.next:
# 				current = current.next
# 			current.next = new_node
# 		else:
# 			self.head = new_node
#
# 	def print(self):
# 		current_node = self.head
# 		while current_node:
# 			print(current_node.value)
# 			current_node = current_node.next
#
# 	def current_sum(self, value):
# 		current_sum = 0
# 		current = value
# 		while current:
# 			current_sum += current.value
# 			current = current.next
# 		return current_sum
#
# 	def max_sum(self):
# 		max_sum = self.current_sum(self.head)
# 		current = self.head.next
# 		# current_sum = 0
# 		while current:
# 			current_sum = self.current_sum(current)
# 			current = current.next
# 			if current_sum > max_sum:
# 				max_sum = current_sum
# 		return max_sum
#
#
# n = int(input())
# ll = LinkedList()
# val = 0
#
# s = input().split()
# for _ in s:
# 	ll.append(int(_))
#
# val = ll.head.value
# print(ll.max_sum())
#


def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


n = int(input())
arr = list(map(int, input().split()))

result = max_subarray_sum(arr)
print(result)
