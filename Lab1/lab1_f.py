def is_prime(n):
    r = int(n/2)+1
    if n > 1:
        for i in range(2, r):
            if n % i == 0:
                return False
        return True
    else:
        return False


n = int(input())

count = 0
num = 0
while count < n:
    num += 1
    if is_prime(num):
        count += 1
    if count == n:
        print(num)
        break
