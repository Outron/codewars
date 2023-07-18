# Build a pyramid-shaped tower, as an array/list of strings, given a positive
# integer number of floors.A tower block is represented with "*" character.

def tower_builder(n_floors):
    lis = []
    floor = ' '
    for i in range(n_floors):
        s = '*' * (i*2 + 1)
        f = ' ' * (n_floors - i - 1)
        floor = f + s + f
        lis.append(floor)

    return lis

print(tower_builder(3))
