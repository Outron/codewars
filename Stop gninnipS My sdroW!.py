def spin_words(sentence):
    sentence = sentence.split(' ')
    z = ''
    for i in sentence:
        if len(i) > 4:
            i = str(i[::-1])
            z = z+i + ' '
        else:
            z += i + ' '
    return z.rstrip()
sen = "Hey fellow warriors"
print(spin_words(sen))