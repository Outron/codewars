def shortcut(s):
    result = ""
    letters = ("a", "e", "i", "o", "u")
    for letter in letters:
        if letter in letters:
            s = s.replace(letter,"")
    return s

s = "hello"
print(shortcut(s))
