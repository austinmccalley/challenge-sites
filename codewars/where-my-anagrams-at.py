import collections

def anagrams(word, words):
    wl = list(word)
    c = collections.Counter(wl)
    
    res = []
    for w in words:
        cwl = list(w)
        cw = collections.Counter(cwl)
        if cw == c:
            res.append(w)
    return res