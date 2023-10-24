from collections import deque

dq = deque()


while True:
    action = input().split()
    if len(action) == 1:
        if action[0] == '!':
            break
        elif action[0] == '*':
            if len(dq) > 1:
                summa = dq.popleft() + dq.pop()
                print(summa)
            elif len(dq) == 1:
                summa = dq.pop() * 2
                print(summa)
            else:
                print('error')
    if len(action) == 2:
        if action[0] == '+':
            dq.appendleft(int(action[1]))
        elif action[0] == '-':
            dq.append(int(action[1]))

