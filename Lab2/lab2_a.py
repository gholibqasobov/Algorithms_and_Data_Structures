n = int(input())
nearest_number_list = [int(num) for num in input().split()]
k = int(input())

offset = 0
min_distance = abs(nearest_number_list[0] - k)

for i in range(0, len(nearest_number_list)):
    if abs(nearest_number_list[i] - k) < min_distance:
        min_distance = abs(nearest_number_list[i] - k)
        offset = i

print(offset)
