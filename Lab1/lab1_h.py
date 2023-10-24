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
flag = 'YES' if is_prime(n) else 'NO'
print(flag)