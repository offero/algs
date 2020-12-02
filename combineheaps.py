'''
Algorithms - Udi Manber
4.13 Combine heaps in O(log m+n) time
'''

def combineheaps(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.v > b.v:
        a,b = b,a
    l,r = a.l, a.r
    a.r = b
    a.l = combineheaps(l,r)
    return a


class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

def printheap(r):
    stack = [r]
    while stack:
        n = stack.pop(0)
        if n is None:
            print(n)
            continue
        print(n.v)
        if n.l or n.r:
            stack.append(n.l)
            stack.append(n.r)

def main():
    a = Node(1,
            Node(3, Node(7), Node(9)),
            Node(5, Node(11), Node(13)),
            )
    b = Node(2,
            Node(4, Node(8), Node(10)),
            Node(6, Node(12), Node(14))
            )

    # c = Node(3, Node(7), Node(9))
    # d = Node(5, Node(11), Node(13))

    printheap(combineheaps(a, b))

if __name__ == "__main__":
    main()
