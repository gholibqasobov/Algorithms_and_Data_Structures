# import sys
#
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#
#     def print(self):
#         current = self.head
#         while current:
#             sys.stdout.write(str(current.value) + ' ')
#             current = current.next
#
#     def pop_front(self):
#         if self.head:
#             temp = self.head
#             self.head = self.head.next
#             return temp.value
#
#     def shift(self, k, n):
#         k = k % n
#         for _ in range(k):
#             self.append(self.pop_front())
#
#
# ll = LinkedList()
#
#
# def get_str(): return list(map(str, sys.stdin.readline().strip().split()))
# def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
#
#
# n, k = get_ints()
# string = get_str()
#
# for i in string:
#     ll.append(i)
#
# ll.shift(k, n)
# ll.print()


from collections import deque

class LinkedList:
    def __init__(self):
        self.deque = deque()

    def append(self, data):
        self.deque.append(data)

    def pop_front(self):
        if self.deque:
            return self.deque.popleft()

    def shift(self, k):
        k = k % len(self.deque)
        self.deque.rotate(-k)

    def print(self):
        print(" ".join(map(str, self.deque)))

# Main code
n, k = map(int, input().split())
string = input().split()

ll = LinkedList()

for i in string:
    ll.append(i)

ll.shift(k)
ll.print()
