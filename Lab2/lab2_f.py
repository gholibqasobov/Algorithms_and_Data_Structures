class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        current = self.head
        position = 0
        if index == position:
            self.insert_at_begin(data)
        else:
            while current is not None and position+1 != index:
                current = current.next
                position += 1

            if current is not None:
                new_node.next = current.next
                current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next


n = int(input())
linked_list = LinkedList()
for i in range(n):
    linked_list.insert(int(input()))

data = int(input())
position = int(input())
linked_list.insert_at_index(data, position)
linked_list.print_list()