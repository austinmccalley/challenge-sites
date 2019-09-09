
def checkList(l, nb):
    li = list(range(1, len(l)+1))

    for i in reversed(list(range(len(l)))):

        e = l[i]
        # i is index
        # e is element
        diff_i = i - li.index(e)
        # print(diff_i)
        if l == li:
            print(nb)
            break
        if diff_i > 0:
            continue
            # Got moved backwards!

        if diff_i < 0 and abs(diff_i) < 3:
            # This number bribed forwards

            # print('Num bribed forward', e, diff_i)
            nb += abs(diff_i)

            # print(q)
            q.pop(i)
            q.insert(i-diff_i, e)
            # print(q)

        elif abs(diff_i) >= 3 and diff_i < 0:
            print('Too chaotic')
            break

        if i == 0 and nb != 0:
            checkList(l, nb)


# Complete the minimumBribes function below.
def minimumBribes(q):
    lq = len(q)
    qi = list(range(1, lq+1))
    # print('Initial Queue', qi)
    # print('After Bribes', q)

    nb = 0

    for i in reversed(list(range(lq))):
        # for i, e in reversed(list(enumerate(q))):
        e = q[i]
        # i is index
        # e is element
        # print(e)
        # print(qi[i])
        diff_i = i - qi.index(e)
        # print(diff_i)
        if diff_i > 0:
            continue
            # Got moved backwards!

        if diff_i < 0 and abs(diff_i) < 3:
            # This number bribed forwards

            # print('Num bribed forward', e, diff_i)

            nb += abs(diff_i)

            # print(q)

            q.pop(i)
            q.insert(i-diff_i, e)
            # print(q)
        elif abs(diff_i) >= 3 and diff_i < 0:
            print('Too chaotic')
            break

        if i == 0 and nb != 0:
            checkList(q, nb)


q1 = [5, 1, 2, 3, 7, 8, 6, 4]
q2 = [1, 2, 5, 3, 7, 8, 6, 4]
q3 = [1, 2, 5, 3, 4, 7, 8, 6]
q4 = [2, 1, 5, 3, 4]
q5 = [2, 5, 1, 3, 4]

queues = [q1, q2, q3, q4, q5]

for q in queues:
    minimumBribes(q)

# minimumBribes(q1)
