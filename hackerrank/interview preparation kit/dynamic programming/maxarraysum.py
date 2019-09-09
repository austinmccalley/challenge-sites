import math


def get_next_nonadjenct(ind, n):
    for la in range(ind, n):
        di = la - ind
        if di > 1 and ind != la:
            # print(ind, la, di, n)
            print(ind, la)

            return [ind, get_next_nonadjenct(la, n)]
            break
        elif (n-1) == la and di != 1:
            return la


def nonadjencts(ind, n):
    if ind + 2 < n:
        return nonadjencts(ind + 2, n)
    elif ind == n:
        return ind
    else:
        print(ind, n)


# maxSubsetSum([-2,1,3,-4,5])

# [0, 2, 4], [0, 2], [0, 3], [0, 4], [1, 3], [1, 4], [2, 4]

#       0  1  2   3  4
arr = [-2, 1, 3, -4, 5]
for ind in range(len(arr)):
    # print(get_next_nonadjenct(ind, len(arr)))
    print(nonadjencts(ind, len(arr)))
