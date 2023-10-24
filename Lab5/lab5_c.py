import heapq

def max_stadium_earnings(n, x, seats):
    max_earnings = 0
    max_heap = [(-seats[i], i) for i in range(n)]
    heapq.heapify(max_heap)

    while x > 0:
        max_seats, row = heapq.heappop(max_heap)
        max_seats = -max_seats
        price = max_seats
        max_earnings += price
        x -= 1

        if max_seats > 1:
            heapq.heappush(max_heap, (-(max_seats - 1), row))

    return max_earnings


n, x = map(int, input().split())
seats = list(map(int, input().split()))


result = max_stadium_earnings(n, x, seats)
print(result)
