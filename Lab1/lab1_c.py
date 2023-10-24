"""
this problem requires the stack to be used


take two strings
keep adding each char to a stack
if char is #, pop from the stack

in the end, check for the similarity
"""

s1, s2 = input().split()
stack1 = []
stack2 = []

for ch in s1:
    if len(stack1) != 0 and ch == '#':
        stack1.pop()
    else:
        stack1.append(ch)

for ch in s2:
    if len(stack2) != 0 and ch == '#':
        stack2.pop()
    else:
        stack2.append(ch)

print('Yes' if stack1 == stack2 else 'No')
