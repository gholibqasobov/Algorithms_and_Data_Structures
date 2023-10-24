"""
Problem: find the least possible capacity
Condition: <= f-number of trips possible, use binary-search
"""
n, f = map(int, input().split())
children = list(map(int, input().split()))

"""
Algorithm: 
    find the mid-capacity using binary search
        check if mid capacity can handle f-trips
            if so, move the upper bound down till the minimum capacity is found
                meaning, left == right
            return left -> minimum capacity
    here: need to check if mid_capacity can handle number of trips:
        sum up all required trips to islands given mid capacity 
            round up the numbers using the equation (children_count + capacity - 1) // capacity
                the formulas checks number of trips: ex. if children are 1. number of trips will be 3: (11 + 5-1)//5 = 3
                every child will receive a gift
        compare it to desired number of trips
        
"""


def can_deliver(children, capacity, trips):
    assumed_trips = 0
    for children_count in children:
        assumed_trips += (children_count + capacity - 1) // capacity
    return assumed_trips <= trips


def mid_capacity(children, trips):
    left, right = 1, max(children)
    while left <= right:
        mid = (left + right) // 2
        if can_deliver(children, mid, trips):
            right = mid - 1
        else:
            left = mid + 1
    return left


print(mid_capacity(children, f))
