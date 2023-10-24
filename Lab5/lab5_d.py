import heapq

def mix_mixtures(n, m, densities):
    heapq.heapify(densities)
    operations = 0

    while densities[0] < m:
        if len(densities) < 2:
            return -1

        least_density = heapq.heappop(densities)
        second_least_density = heapq.heappop(densities)
        new_density = least_density + 2 * second_least_density
        heapq.heappush(densities, new_density)
        operations += 1

    return operations


n, m = map(int, input().split())
densities = list(map(int, input().split()))


result = mix_mixtures(n, m, densities)
print(result)
