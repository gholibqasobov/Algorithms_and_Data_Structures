import heapq


def find_minimum_cost(sizes):
    cost = 0
    heap = list(sizes)
    heapq.heapify(heap)

    while len(heap) > 1:
        array1 = heapq.heappop(heap)
        array2 = heapq.heappop(heap)
        merge_cost = array1 + array2
        cost += merge_cost
        heapq.heappush(heap, merge_cost)

    return cost


# Input
n = int(input())
sizes = list(map(int, input().split()))

# Calculate and print the minimum cost
result = find_minimum_cost(sizes)
print(result)
