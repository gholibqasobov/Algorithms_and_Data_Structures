import sys

n, k = list(map(int, sys.stdin.readline().strip().split()))
arr = list(map(int, sys.stdin.readline().strip().split()))


def block_count(houses, max_ghouls):
    blocks = 1
    current_sum = 0
    for ghouls in houses:
        current_sum += ghouls
        if current_sum > max_ghouls:
            blocks += 1
            current_sum = ghouls
    return blocks


def binary_search(arr, k):
    left = max(arr)
    right = sum(arr)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if block_count(arr, mid) <= k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


print(binary_search(arr, k))
