import sys


def binary_search(arr, goal):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]
        if guess > goal:
            right = mid - 1
        elif guess < goal:
            left = mid + 1
        else:
            return mid
    return -1


n = input()
arr = list(map(int, sys.stdin.readline().strip().split()))
x = int(input())

statement = 'Yes' if binary_search(arr, x) != -1 else 'No'
print(statement)
