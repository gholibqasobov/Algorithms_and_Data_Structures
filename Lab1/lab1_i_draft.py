# n = int(input())
# str = [ch for ch in input()]
#
# added_votes = {'K': 0, 'S': 0}
# removed_votes = {'K': 0, 'S': 0}
#
# for i in range(n):
#     added_votes[str[i]] += 1
#
# while added_votes['K'] > 0 and added_votes['S'] > 0:
#     if removed_votes[str[0]] > 0:
#         added_votes[str[0]] -= 1
#         removed_votes[str[0]] -= 1
#         str.pop(0)
#     else:
#         if str[0] == 'S':
#             removed_votes['K'] += 1
#         else:
#             removed_votes['S'] += 1
#         str.append(str[0])
#         str.pop(0)
#
# leader = 'KATSURAGI' if added_votes['K'] else 'SAKAYANAGI'
# print(leader)
#

n = int(input())
s = input()

added_votes = {'K': 0, 'S': 0}
removed_votes = {'K': 0, 'S': 0}

for ch in s:
    added_votes[ch] += 1

i = 0
while added_votes['K'] > 0 and added_votes['S'] > 0:
    if removed_votes[s[i]] > 0:
        added_votes[s[i]] -= 1
        removed_votes[s[i]] -= 1
        i += 1
    else:
        if s[i] == 'S':
            removed_votes['K'] += 1
        else:
            removed_votes['S'] += 1
        s += s[i]
        i += 1

leader = 'KATSURAGI' if added_votes['K'] else 'SAKAYANAGI'
print(leader)
