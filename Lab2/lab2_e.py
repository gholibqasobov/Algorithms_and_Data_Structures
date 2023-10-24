import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_duplicates(self):
        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            if next_node and next_node.value == current.value:
                if prev is None:
                    self.head = next_node
                else:
                    prev.next = next_node
                current = next_node
            else:
                prev = current
                current = next_node

    def display(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def length(self):
        current = self.head
        i = 0
        while current:
            i += 1
            current = current.next
        return i


def main():
    ll = LinkedList()
    n = int(input())
    for i in range(n):
        ll.push_front(input())

    ll.remove_duplicates()
    print('All in all:', ll.length())
    print('Students:')
    ll.display()


if __name__ == '__main__':
    main()