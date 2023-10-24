import heapq

q, k = map(int, input().split())
cookies = []
total_cookies = 0

for _ in range(q):
    command = input().split()
    if command[0] == 'insert':
        n = int(command[1])
        heapq.heappush(cookies, n)
        total_cookies += n
        if len(cookies) > k:
            total_cookies -= heapq.heappop(cookies)
    else:
        print(total_cookies)

