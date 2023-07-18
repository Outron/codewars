def get_count(sentence):
    vowels = ['a','e','i','o','u']
    #vowels = "aeiou"
    count = 0
    for i in vowels:
        if i in sentence:
            count = count + sentence.count(i)
    return count

sen = "Should count all vowels"
print(get_count(sen))
