def divisors(integer): #15
    z = []
    for i in range(2,integer-1):
        if integer % i == 0:
            z.append(i)

    if len(z) == 0:
        return str(integer) + " is prime"
    else:
        return z

a = 12
print(divisors(a))
