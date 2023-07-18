def move_zeros(lst):
    nz = []
    z = []
    for i in range(len(lst)):
        if lst[i] != 0:
            nz.append(lst[i])
        else:
            z.append(lst[i])
    return nz + z


lst = [1, 0, 1, 2, 0, 1, 3]
print(move_zeros(lst))
