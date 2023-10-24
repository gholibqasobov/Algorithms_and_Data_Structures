n = int(input())
rivals = sorted(map(int, input().split()))
rounds = int(input())


def upper_bound(arr, goal):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]
        if guess <= goal:
            left = mid + 1
        else:
            right = mid - 1
    return left


prefix_sums = [0] + [sum(rivals[:i+1]) for i in range(n)]
# print(prefix_sums)
# print(prefix_sums[4])

while rounds != 0:
    power = int(input())
    lost_rivals_num = upper_bound(rivals, power)
    print(lost_rivals_num, prefix_sums[lost_rivals_num])
    rounds -= 1

