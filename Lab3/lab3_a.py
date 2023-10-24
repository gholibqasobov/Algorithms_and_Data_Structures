n = int(input())
goals = [int(num) for num in input().split()]

row, column = input().split()
row = int(row)
column = int(column)

dict_arr = dict()
arr = []

for i in range(row):
    num = [int(num) for num in input().split()]
    for j in range(len(num)):
        dict_arr[num[j]] = (i, j)
    if i % 2 == 0:
        arr.extend(num)
    else:
        arr.extend(num[::-1])

arr = arr[::-1]


# Binary search
def binary_search(arr, goal):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        guess = arr[mid]
        if guess < goal:
            left = mid + 1
        elif guess > goal:
            right = mid - 1
        else:
            return mid
    return -1


for goal in goals:
    if binary_search(arr, goal) != -1:
        print(*dict_arr[goal])
    else:
        print(-1)
