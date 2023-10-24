import sys


"""
they boundaries will be inputted in while loop
"""

"""
sort the array

get lower_bound

get upper_bound

result = upper_bound - lower_bound + 1

"""


def lower_bound(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            # left = mid + 1
             right = mid - 1
        else:
            left = mid + 1
    return left


def upper_bound(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def check_overlap(l1, r1, l2, r2):
    # if r1 >= l2 and r2 >= l1:
    #     # overlapping_region = [max(l1, l2), min(r1, r2)]
    #     l1, r1, l2, r2 = l2, r2, l1, r1
    #
    #     # Trim intervals
    #     if l2 > l1:
    #         r1 = l2 - 1
    #     else:
    #         l1 = r2 + 1
    #
    #     if r2 > r1:
    #         l2 = r1 + 1
    #     else:
    #         r2 = l1 - 1
    #
    # return l1, r1, l2, r2
    if (r1 - l1) < (r2 - l2):
        r1, r2 = r2, r1
        l1, l2 = l2, l1

    if r2 <= r1 and l2 >= l1:
        return [l1, r1]
    elif r1 >= r2 >= l1 > l2:
        r2 = l1 - 1
    elif r2 > r1 > l2:
        l2 = r1 + 1

    return [l1, r1, l2, r2]


n, q = list(map(int, sys.stdin.readline().strip().split()))
query = sorted(list(map(int, sys.stdin.readline().strip().split())))
while q != 0:
    boundary = list(map(int, sys.stdin.readline().strip().split()))
    if len(check_overlap(*boundary)) > 2:
        l1, r1, l2, r2 = check_overlap(*boundary)
        sol = ((upper_bound(query, r1) - lower_bound(query, l1)) + 1) + \
              ((upper_bound(query, r2) - lower_bound(query, l2)) + 1)
    else:
        l1, r1 = check_overlap(*boundary)
        sol = ((upper_bound(query, r1) - lower_bound(query, l1)) + 1)

    print(sol)
    q -= 1

