def triangular(n):
    if n < 0:
        return 0
    return int((n*(n+1))/2)

n = 3
print(triangular(n))