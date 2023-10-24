import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # def delete_at_index(self, index):
    #     position = 0
    #     if index == position:
    #         self.head = self.head.next
    #         return
    #
    #     current = self.head
    #     if current.next and position+1 != index:
    #         current = current.next
    #         position += 1
    #
    #     if current.next:
    #         current.next = current.next.next

    def print(self):
        current = self.head
        while current:
            sys.stdout.write(str(current.value) + ' ')
            current = current.next
        sys.stdout.write('\n')

    def delete_odd(self):
        if self.head is None:
            return

        prev = self.head
        now = self.head.next

        while prev is not None and now is not None:
            prev.next = now.next

            now = None

            prev = prev.next

            if prev is not None:
                now = prev.next


def main():
    ll = LinkedList()

    n = int(input())

    def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

    arr = get_ints()

    for i in arr:
        ll.append(i)

    ll.delete_odd()
    ll.print()


if __name__ == '__main__':
    main()

