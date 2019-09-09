"""
Runtime: 88 ms, faster than 16.27% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.1 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
https://leetcode.com/problems/add-two-numbers/submissions/
"""

def addTwoNumbers(l1, l2):
        cn1 = l1
        cn2 = l2
        lnum1 = []
        lnum2 = []
        while cn1 != None:
            lnum1.append(cn1.val)
            cn1 = cn1.next
        while cn2 != None:
            lnum2.append(cn2.val)
            cn2 = cn2.next

        lnum1.reverse()
        lnum2.reverse()

        num1 = int("".join([str(i) for i in lnum1]))
        num2 = int("".join([str(i) for i in lnum2]))
        tnum = num1 + num2

        ltnum = [int(i) for i in str(tnum)]

        nodes = []
        for i in range(len(ltnum)):
            if i == 0:
                node = ListNode(ltnum[i])
                nodes.append(node)
            else:
                node = ListNode(ltnum[i])
                node.next = nodes[i-1]
                nodes.append(node)
        return nodes[len(nodes)-1]


class ListNode:
    def __init__(self, x, ):
        self.val = x
        self.nexty = None
