def is_prime(n):
    r = int(n/2)+1
    if n > 1:
        for i in range(2, r):
            if n % i == 0:
                return False
        return True
    else:
        return False


def nth_prime(n):
    count = 0
    num = 0
    prime_num = 0
    while True:
        num += 1
        if is_prime(num):
            count += 1
        if count == n:
            prime_num = num
            break
    return prime_num


# get a number of nth prime
"""
make a list of prime numbers
from its indices extract nth prime and return its value
"""
prime_list = []
n = int(input())
num = 0
count = 0
while True:
    num += 1
    if is_prime(num):
        prime_list.append(num)
        if is_prime(prime_list.index(num)):
            count += 1
        if count == n:
            print(prime_list[-2])
            break
