def Descending_Order(num):
    nl = list(str(num))
    nl.sort(reverse=True)
    return int(''.join(nl))