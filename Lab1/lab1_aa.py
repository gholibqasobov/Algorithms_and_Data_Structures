n = int(input())

ppl_q = [int(num) for num in input().split()]
ppl_age = [-1] * n
stack = []

for i in range(n-1, -1, -1):
    while stack and ppl_q[i] <= ppl_q[stack[-1]]:
        ppl_age[stack.pop()] = ppl_q[i]

    stack.append(i)

print(*ppl_age)
