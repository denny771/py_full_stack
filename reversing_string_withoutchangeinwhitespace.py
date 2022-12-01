def func(word):
    result = [0]*len(word)
    for i in range (len(word)):
        if (word[i] == ' '):
            result[i] = ' '
    j = len(word) - 1
    for i in range(len(word)):
        if (word[i]!=' '):
            if result[j] == ' ':
                j = j-1
            result[j] = word[i]
            j-=1
    return ''.join(result)

print(func("I code in python"))
