import string

def alphabet_position(text):
    characters = list(text.lower())
    res = []
    for char in characters:
        if char in string.ascii_lowercase:
            val = string.ascii_lowercase.index(char) +1
            res.append(val)
    print(' '.join(map(str, res)))
    return (' '.join(map(str, res)))
    
alphabet_position("The sunset sets at twelve o' clock.")