import collections


def lengthOfLongestSubstring(s):
    sl = list(s)

    if len(sl) == 1:
        return 1

    print(sl)
    max__len = 0
    for i in range(1, len(sl)):
        letter = sl[i-1]

        lsl = sl[i:]
        if letter in lsl and i != 0:
            ri = sl.index(letter)
            if max__len < len(sl[:ri]):
                print(sl[:ri])
                max__len = len(sl[:ri])

    if len(sl) == 2 and max__len == 0:
        return 2

    return max__len


test_cases = ["abcabcbb", "aab"]

for test in test_cases:
    print(lengthOfLongestSubstring(test))
