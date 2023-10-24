# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# def insert(root, value):
#     if root is None:
#         return Node(value)
#     if root.value > value:
#         root.left = insert(root.left, value)
#     else:
#         root.right = insert(root.right, value)
#     return root

def insert(root, value):
    if root is None:
        return Node(value)
    if root.value > value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


# def print_inorder(root):
#     if root is not None:
#         print_inorder(root.left)
#         print(root.value, end=' ')
#         print_inorder(root.right)


def print_inorder(root):
    if root is not None:
        print_inorder(root.left)
        print(root.value, end=' ')
        print_inorder(root.right)


root = None
root = insert(root, 1)
insert(root, 2)
insert(root, 0)
print_inorder(root)
