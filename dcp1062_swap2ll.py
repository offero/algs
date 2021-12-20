'''
DCP #1062
Given the head of a singly linked list, swap every 2 nodes and return its head.
Ex: 1 -> 2 -> 3 -> 4
    2 -> 1 -> 4 -> 3

Note: This would be really simple if we just swapped the values and not the node
pointers themselves, but I'm doing it the hard way by swapping pointers because
that's what I think the intent of the question is asking for.
'''
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next_node: Node

def swap_node(a, b, c, d: Node):
    """
    a and d can be None
    b and c must be Node instances
    """
    if a is not None:
        a.next_node = c
    c.next_node = b
    b.next_node = d

def swap2(head):
    if head.next_node is None:
        return head

    new_head = head.next_node
    node = head
    prev = None
    while node is not None and node.next_node is not None:
        swap_node(prev, node, node.next_node, node.next_node and node.next_node.next_node)
        prev = node
        node = node.next_node
    return new_head

def print_ll(head):
    node = head
    values = []
    while node is not None:
        values.append(str(node.value))
        node = node.next_node
    print('->'.join(values))


def ex1():
    ll = Node(1,
            Node(2,
                Node(3,
                    Node(4, None))))
    print_ll(ll)
    new_ll = swap2(ll)
    print_ll(new_ll)

def ex2():
    ll = Node(1,
            Node(2,
                Node(3,
                    Node(4,
                        Node(5, None)))))
    print_ll(ll)
    new_ll = swap2(ll)
    print_ll(new_ll)

if __name__ == "__main__":
    ex2()
