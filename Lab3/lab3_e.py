def count_sheeps(paddock_size, sheeps):
    count = 0
    for sheep in sheeps:
        x1, y1, x2, y2 = sheep
        if 0 <= x1 <= paddock_size and 0 <= y1 <= paddock_size and x2 <= paddock_size and y2 <= paddock_size:
            count += 1
    return count


def binary_search_min_side_length(N, K, sheeps):
    left, right = 0, 2 * 10 ** 9

    while left < right:
        mid = (left + right) // 2
        if count_sheeps(mid, sheeps) >= K:
            right = mid
        else:
            left = mid + 1

    return left


# Input
N, K = map(int, input().split())
sheeps = [list(map(int, input().split())) for _ in range(N)]

# Output
result = binary_search_min_side_length(N, K, sheeps)
print(result)
