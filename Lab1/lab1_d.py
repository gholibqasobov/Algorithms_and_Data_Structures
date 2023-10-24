"""
String is balanced:
empty string

is substring s and t are balanced, string st(concatenation) is also balanced

if string is balanced, any string xsx is balanced

"""

"""
may be

store in the stack, as long as the similar ch to the last one has come, delete.
if stack is empty, it is balanced, else no

sbaabsss

yes
sbabasss
no
"""

s = input()
stack = []
msg = ''
if len(s) == 0:
    msg = 'No'
else:
    for ch in s:
        if len(stack) != 0 and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if len(stack) == 0:
        print('Yes')
    else:
        print('No')

