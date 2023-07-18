def strip_comments(strng, markers):
    lst = strng.split('\n')
    words = []
    for i in lst:
        s = ''
        for char in i:
            if char in markers:
                break
            else:
                s += char
        words.append(s.strip())
    return "\n".join(words)

markers = ['#', '!']
strng = 'apples, pears # and bananas\ngrapes\nbananas !apples'

print(strip_comments(strng,markers))
