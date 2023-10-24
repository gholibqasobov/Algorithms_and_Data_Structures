class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_data = Node(data)

        if self.head is None:
            self.head = new_data
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_data

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_el = current.next
            current.next = prev
            prev = current
            current = next_el
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, data, index):
        position = 0
        if position == index:
            self.push_front(data)
        else:
            new_node = Node(data)
            current = self.head
            while current is not None and position+1 != index:
                current = current.next
                position += 1

            if current is not None:
                new_node.next = current.next
                current.next = new_node

    def pop_font(self):
        if self.head:
            self.head = self.head.next

    def remove_at_index(self, index):
        position = 0
        if position == index:
            self.pop_font()
        else:
            current = self.head
            while current is not None and position+1 != index:
                current = current.next
                position += 1
            if current is not None:
                current.next = current.next.next

    def reverse_list(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = current.next


ll = LinkedList(Node(1))
ll.append(2)
ll.append(3)
ll.display()
print()
ll.reverse_list()
ll.display()
print()
ll.insert_at_index(8, 3)
ll.display()
print()
# ll.remove_at_index(1)
ll.display()

ll.reverse_list()

ll.display()
