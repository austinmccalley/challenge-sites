import collections

def is_isogram(string):
    if string == "":
        return True
    
    s = string.lower()
    sl = list(s)
    c = collections.Counter(sl)

    for char in sl:
        if c[char] > 1:
            return False
    return True
