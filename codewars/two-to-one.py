"""
A big issue I faced with this problem is I thought we were looking at each string
and then finding unique and sorted off of that then returning the longer one. The 
question was misguiding.
"""
def longest(s1, s2):
    ts = list(set(s1+s2))
    ts.sort()
    return (''.join(ts))
