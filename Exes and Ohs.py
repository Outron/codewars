def xo(s):
    Xcount = 0
    Ocount = 0
    s = s.lower()

    for i in s:
        if i not in s:
            return True
        if i == 'x':
            Xcount += 1
        if i == 'o':
            Ocount += 1

    if Xcount == Ocount:
        return True
    else:
        return False

s = "zpzpzp"
print(xo(s))

# Better option
# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')


