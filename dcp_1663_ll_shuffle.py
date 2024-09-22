'''
# Problem
Given a linked list, uniformly shuffle the nodes.
What if we want to prioritize space over time?


# Solution approach

Each element has a 1/(N-k) chance of being swapped with the k'th position.
Count the linked list (N)
For each position (k),
    Generate a random number [0, 1)
    Set accumulator to 1/(N-k)
    Loop through the linked list from that position to the end
        if rand < acc:
            swap
        add 1/(N-k) to acc
'''
from dataclasses import dataclass, field
from random import random

@dataclass
class Node:
    data: int
    next: "Node" = field(default=None)

def count_ll(node):
    n = 1
    while node.next:
        node = node.next
        n += 1
    return n

def ushuffle_ll(head):
    N = count_ll(head)
    k = 0
    ap, a = None, head
    bp, b = None, head
    # assign to each position
    for pos in range(N):
        # print_ll(head)
        r = random()
        # each node can be assigned to position
        for i, k in enumerate(range(pos, N)):
            val = (1/(N-pos)) * (i+1)
            # print (a.data, b.data, r, val)
            if r <= val:
                # print(f"swap {k} into {pos}")
                # swap b and a
                if a == b:
                    break

                if a == head:
                    head = b

                if ap:
                    ap.next = b
                if bp:
                    bp.next = a

                a.next, b.next = b.next, a.next

                ap, a = bp, b

                # exit loop
                break;
            else:
                # increment b
                bp = b
                b = b.next
        # increment a
        ap = a
        a = a.next
        bp = ap
        b = a
    return head


def build_ll(size=10):
    head = Node(0)
    cur = head
    for x in range(1, size+1):
        cur.next = Node(x)
        cur = cur.next
    return head

def print_ll(node):
    values = [node.data]
    while (node.next):
        node = node.next
        values.append(node.data)
    print(' '.join(map(str, values)))

ll = build_ll()
# print_ll(ll)
new_head = ushuffle_ll(ll)
# print_ll(new_head)


size = 10
agg = [0] * size
samples = 10000
for _ in range(samples):
    ll = build_ll(size)
    head = ushuffle_ll(ll)
    node = head
    for i in range(size):
        agg[i] += node.data
        node = node.next

print([x/samples for x in agg])
