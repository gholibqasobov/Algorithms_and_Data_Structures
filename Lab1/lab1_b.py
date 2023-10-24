# n = int(input("Enter length: "))
#
# people_queue = []
# for i in range(n):
#     age = int(input())
#     people_queue.append(age)
#
# closest_age = [-1] * n
# stack = []
#
#
# while len(people_queue) != 0:
#     p1 = people_queue.pop()
#     check_people = people_queue.copy()
#     while len(check_people) != 0:
#         p2 = check_people.pop()
#         if p2 < p1:
#             closest_age.append(p2)
#             break
#     else:
#         closest_age.append(-1)
#
#
# print(*closest_age[::-1])
#
n = int(input())

ppl_q = [int(num) for num in input().split()]
ppl_age = [-1] * n
stack = []

for i in range(n-1, -1, -1):
    while stack and ppl_q[i] <= ppl_q[stack[-1]]:
        ppl_age[stack.pop()] = ppl_q[i]

    stack.append(i)

print(*ppl_age)
