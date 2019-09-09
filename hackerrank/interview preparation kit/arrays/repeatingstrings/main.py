# Complete the repeatedString function below.
def repeatedString(s, n):

    if s == 'a':
        return n

    ls = len(s) # Length of the string

    wr = n//ls # How many times to repeat to get to n  
    fr = n % ls # Get the remainder times we have to split the string by 

    print(wr)
    print(fr)

    org_s_ac = list(s).count('a')

    f_ac = list(s[:fr]).count('a')

    a_count = org_s_ac*wr + f_ac
    return a_count

s = "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq"
n = 549382313570


print(repeatedString(s,n))