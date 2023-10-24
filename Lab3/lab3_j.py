"""
minimum number k stealing all golds
"""
import sys

"""
least time = 1
most time = max(list)

we will find the mid-k by binary search
    check if it satisfies by another function
    if so, reduce the k amount
    else left = mid + 1
    return left
"""


def check_steal_time(gold_bars, k, hours):
    assumed_time = 0
    for gold_bar in gold_bars:
        assumed_time += (gold_bar + k - 1)//k
    return assumed_time <= hours


def minimum_k_golds(arr, hours):
    left, right = 1, max(arr)
    while left <= right:
        mid = (left + right) // 2
        if check_steal_time(arr, mid, hours):
            right = mid - 1
        else:
            left = mid + 1
    return left


n, hours = list(map(int, sys.stdin.readline().strip().split()))
gold_bag = list(map(int, sys.stdin.readline().strip().split()))
print(minimum_k_golds(gold_bag, hours))
