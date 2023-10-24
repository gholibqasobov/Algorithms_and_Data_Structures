import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        return 'ok'

    def add_back(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node
            new_node.next = None
        return 'ok'

    def erase_front(self):
        if self.head:
            temp = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = temp.next
                temp.next.prev = None
                temp.next = None
            return temp.value
        else:
            return 'error'

    def erase_back(self):
        if self.tail:
            temp = self.tail
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = temp.prev
                temp.prev.next = None
                temp.prev = None
            return temp.value
        else:
            return 'error'

    def front(self):
        if self.head is not None:
            print(self.head.value)
        else:
            print('error')

    def back(self):
        if self.tail is not None:
            print(self.tail.value)
        else:
            print('error')

    def display(self):
        current = self.head
        while current:
            sys.stdout.write(str(current.value) + ' ')
            current = current.next
        sys.stdout.write('\n')

    def clear(self):
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            current.prev = None
            current = next_node
        self.head = None
        self.tail = None
        return 'ok'


def main():
    dll = DoublyLinkedList()

    def get_str(): return list(map(str, sys.stdin.readline().strip().split()))

    while True:
        s = get_str()
        if s[0] == 'exit':
            sys.stdout.write('goodbye')
            break
        elif s[0] == 'add_front':
            print(dll.add_front(s[1]))
        elif s[0] == 'add_back':
            print(dll.add_back(s[1]))
        elif s[0] == 'erase_front':
            print(dll.erase_front())
        elif s[0] == 'erase_back':
            print(dll.erase_back())
        elif s[0] == 'front':
            dll.front()
        elif s[0] == 'back':
            dll.back()
        elif s[0] == 'clear':
            print(dll.clear())


if __name__ == '__main__':
    main()


