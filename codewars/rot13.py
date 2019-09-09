import string

def rot13(message):
    ml = list(message)

    res = []
    ans = []
    for letter in ml:
        if letter in string.ascii_lowercase:
            res.append((string.ascii_lowercase.index(letter)+13)%26)
        elif letter in string.ascii_uppercase:
            res.append('u'+str((string.ascii_uppercase.index(letter)+13)%26))
        else:
            res.append(letter)
    for r in res:
        if not isinstance(r, int):
            if 'u' in r:
                ans.append(string.ascii_uppercase[int(r[1:])])
            else:
                ans.append(r)
        else:
            ans.append(string.ascii_lowercase[r])

    return (''.join(ans))


print(rot13("Avoid success at all costs!"))
