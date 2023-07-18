def disemvowel(string_):
    vowels = ['a', 'o', 'e', 'u', 'i', 'A', 'O', 'E', 'U', 'I']

    z = string_.lower()
    for i in string_:
        if i in vowels:
           z = z.replace(i, '')
    return z.strip()

s = "No offense but,\nYour writing is among the worst I've ever read"
print(disemvowel(s))
