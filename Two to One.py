def longest(a1, a2):
    s = set(a1 + a2)
    letters = sorted(s)
    return ''.join(letters)

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

print(longest(a,b))
