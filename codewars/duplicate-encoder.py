import collections

def duplicate_encode(word):
    word = word.lower()
    wl = list(word)
    counter = collections.Counter(wl)

    res = []
    for char in wl:
        if counter[char] > 1:
            res.append(')')
        else:
            res.append('(')
    return ''.join(res)
    

duplicate_encode('Success')