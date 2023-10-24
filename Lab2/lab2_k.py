# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#
#     def push_back(self, value):
#         new_node = Node(value)
#         if not self.head:
#             self.head = new_node
#         else:
#             self.tail.next = new_node
#         self.tail = new_node
#         self.length += 1
#
#     def pop_front(self):
#         if not self.head:
#             return 'error'
#         front = self.head
#         self.head = self.head.next
#         self.length -= 1
#         if not self.head:
#             self.tail = None
#         return front.value
#
#     def pop_back(self):
#         if not self.head:
#             return 'error'
#         if self.head == self.tail:
#             value = self.head.value
#             self.head = None
#             self.tail = None
#             self.length -= 1
#             return value
#         current = self.head
#         while current.next.next:
#             current = current.next
#         back = current.next
#         current.next = None
#         self.tail = current
#         self.length -= 1
#         return back.value
#
#     def peek_front(self):
#         if self.head is None:
#             return
#         else:
#             return self.head.value
#
#     def peek_back(self):
#         if self.tail is None:
#             return
#         else:
#             return self.tail.value
#
#     def print(self):
#         current = self.head
#         i = 0
#         while current:
#             print(current.value, end=' ')
#             current = current.next
#             i += 1
#         print()
#         print(i)
#
#
# n = int(input())
#
# for _ in range(n):
#     dll = DoublyLinkedList()
#     k = int(input())
#     s = input().split()
#
#     for i in s:
#         dll.push_back(i)
#
#         while dll.head != dll.tail and dll.peek_front() == dll.peek_back():
#             dll.pop_back()
#             dll.pop_front()
#         if dll.length == 0:
#             print(-1, end=' ')
#         else:
#             print(dll.peek_front(), end=' ')
#     print()
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head
#         self.frequency = dict()
#
#     def append(self, data):
#         new_node = Node(data)
#         self.frequency[data] = self.frequency.get(data, 0) + 1
#
#         if self.head is None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#
#     def display(self):
#         current = self.head
#         while current:
#             print(current.value)
#             current = current.next
#
#     def first_unique(self):
#         current = self.head
#         first = False
#         while current:
#             if self.frequency[current.value] == 1:
#                 first = True
#                 break
#             current = current.next
#         if first:
#             return current.value
#         else:
#             return -1
#
#
# n = int(input())
# for i in range(n):
#     c = int(input())
#     s = input().split()
#     ll = LinkedList()
#     output = []
#     for ch in s:
#         ll.append(ch)
#         output.append(ll.first_unique())
#     print(*output)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def push(self, val):
#         new_node = Node(val)
#         if self.head is None:
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#
# def main():
#     n = int(input())
#
#     while n > 0:
#         c = int(input())
#         linked_list = LinkedList()
#         frequency_map = {}
#
#         while c > 0:
#             val = input()
#             linked_list.push(val)
#             frequency_map[val] = frequency_map.get(val, 0) + 1
#
#             cur = linked_list.head
#             first = False
#             while cur:
#                 if frequency_map[cur.val] == 1:
#                     first = True
#                     break
#                 cur = cur.next
#
#             if first:
#                 print(cur.val, end=" ")
#             else:
#                 print(-1, end=" ")
#
#             c -= 1
#
#         frequency_map.clear()
#         print()
#         n -= 1
#
#
# if __name__ == "__main__":
#     main()

from collections import defaultdict, deque

def find_first_non_repeating_chars(T, test_cases):
    results = []
    for i in range(T):
        N, chars = test_cases[i]
        char_count = defaultdict(int)
        char_queue = deque()
        output = []

        for char in chars:
            char_count[char] += 1
            char_queue.append(char)

            while char_queue and char_count[char_queue[0]] > 1:
                char_queue.popleft()

            if char_queue:
                output.append(char_queue[0])
            else:
                output.append("-1")

        results.append(output)

    return results


T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    chars = input().split()
    test_cases.append((N, chars))

for i in range(T):
    N, chars = test_cases[i]
    output = find_first_non_repeating_chars(1, [(N, chars)])[0]
    print(" ".join(output))

