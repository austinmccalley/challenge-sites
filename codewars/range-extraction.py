def check_next_num(inp, j):
    for i in range(j, len(inp)):
        elm = inp[i]
        if len(inp) > i+1:
            if inp[i+1] == (elm+1):
                check_next_num(inp, i+1)
            else:
                if j == 0:
                    return i
                return i
        else:
            return len(inp)-1

def solution(inp):
    """
    1. Sort inp
    2. Check to see if next in inp slist is the next value
    """

    inp.sort()


    ranges = []
    res = []


    for i in range(len(inp)):
        
        l = check_next_num(inp, i)
        ranges.append([i, l])
        print([i, l])


    seen = []
    for r in ranges:
        si = r[0]
        ei = r[1]

        sv = inp[si]
        ev = inp[ei]
        if ei not in seen:
            if ev == sv:
                res.append(str(ev))
                seen.append(ei)

            if (ev - sv) >= 2:
                        s = str(sv)+'-'+str(ev)
                        res.append(s)
                        seen.append(ei)
            elif (ev-sv) == 1:
                res.append(str(sv))

    return (",".join(res))
    print(ranges)


#Indexs    0  1  2  3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 
solution([-6,-3,-2,-1,0,1,3,4,5,7,8, 9, 10,11,14,15,17,18,19,20])

"""

[0,0], [1,5], [6,13], [14,15], [17, 19]

[[0, 0], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 8], [7, 8], [8, 8], [9, 13], [10, 13], [11, 13], [12, 13], [13, 13], [14, 15], [15, 15], [16, 19]

-6,-3-1,3-5,7-11,14,15,17-20
-6,-3-1,3-5,7-11,14,15,17-20
-6,-3-1,3-5,7-11,14,15,17-20
"""

#Indexes   0  1  2 3 4  5  6  7  8  9
# solution([-3,-2,-1,2,10,15,16,18,19,20])

"""


 [0, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 9]  
[[0, 2], [3, 3], [4, 4], [5, 6], [6, 6], [7, 9]]
[[0, 0], [1, 2], [2, 2], [3, 3], [4, 4], [5, 6], [6, 6], [7, 9], [8, 9], [9, 9]]

-3--1,2,10,15,16,18-20

-3--1,2,10,15,16,18-20
-3,-2,-1,2,10,15,16,18-20

"""