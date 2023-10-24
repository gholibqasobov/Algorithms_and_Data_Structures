import heapq


def last_stone_weight(weights):
    max_heap = [-weight for weight in weights]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        heaviest1 = -heapq.heappop(max_heap)
        heaviest2 = -heapq.heappop(max_heap)

        if heaviest1 != heaviest2:
            new_weight = abs(heaviest1 - heaviest2)
            heapq.heappush(max_heap, -new_weight)

    if len(max_heap) == 0:
        return 0
    else:
        return -max_heap[0]


# Input
N = int(input())
weights = list(map(int, input().split()))

# Calculate and print the weight of the remaining stone
result = last_stone_weight(weights)
print(result)
