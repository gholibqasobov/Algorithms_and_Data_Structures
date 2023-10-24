n = int(input())
arr = [int(num) for num in input().split()]

arr_freq = dict()

for num in arr:
    if num in arr_freq:
        arr_freq[num] += 1
    else:
        arr_freq[num] = 1


max_len = max(values for values in arr_freq.values())

sorted_list = []
for item, value in arr_freq.items():
    if value == max_len:
        sorted_list.append(item)

print(*sorted(sorted_list)[::-1])
