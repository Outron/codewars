def digital_root(n):
    if n == 0:
        return 0
    else:
        return (n-1) % 9 + 1

n = 3423
print(digital_root(n))
