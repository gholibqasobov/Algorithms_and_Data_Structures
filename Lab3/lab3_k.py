# import sys
#
#
# def prefix_sum(arr, integer):
#     return [sum(arr[:i+1]) for i in range(integer)]
#
#
# def minimum_subarray(arr, k):
#     left = 0
#     right = len(arr) - 1
#     minLength = float('inf')
#     while left <= right:
#         mid = (left + right) // 2
#         if sum(arr[0:mid + 1]) >= k:
#             minLength = min(minLength, mid + 1)
#             right = mid - 1
#         else:
#             left = mid + 1
#     return minLength
#
#
# n, k = list(map(int, sys.stdin.readline().strip().split()))
# numbers = list(map(int, sys.stdin.readline().strip().split()))
# print(minimum_subarray(numbers, k))
# # print(prefix_sum(numbers, k))


def minimum_subarray_length(n, k, arr):
    def is_valid_length(length):
        for i in range(n - length + 1):
            current_sum = prefix_sums[i + length - 1] - prefix_sums[i] + arr[i]
            if current_sum >= k:
                return True
        return False

    left, right = 1, n
    result = n  # Initialize with the maximum possible length

    while left <= right:
        mid = (left + right) // 2
        if is_valid_length(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Calculate prefix sums
prefix_sums = [0] * n
prefix_sums[0] = arr[0]
for i in range(1, n):
    prefix_sums[i] = prefix_sums[i - 1] + arr[i]

# Find and print the minimum subarray length
result = minimum_subarray_length(n, k, arr)
print(result)
