import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_bst(root, value):
    if root is None:
        return Node(value)
    if root.value > value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root


def exists_in_bts(root, value):
    whi


def is_path_available(root, path):
    current = root
    for direction in path:
        if direction == 'R' and current.right:
            current = current.right
        elif direction == 'L' and current.left:
            current = current.left
        else:
            return 'NO'
    return 'YES' if exists_in_bts(root, current.value) is not None else 'No'


n, k = list(map(int, sys.stdin.readline().strip().split()))
bst_val = list(map(int, sys.stdin.readline().strip().split()))
root = None
for node in bst_val:
    root = insert_bst(root, node)

for i in range(k):
    path = input()
    print(is_path_available(root, path))




