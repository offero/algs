'''
Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
'''

# class based version
# TODO: array-based version

class Node:
    def __init__(self, label, l=None, r=None):
        self.label = label
        self.l = l
        self.r = r

def invert_tree(node):
    """
    post-order traverse
    """
    if node.l is not None:
        invert_tree(node.l)
    if node.r is not None:
        invert_tree(node.r)
    node.l, node.r = node.r, node.l

def print_tree(node):
    """
    level-order print
    """
    stack = [node]
    while stack:
        node = stack[0]
        stack = stack[1:]
        print(node.label)
        if node.l:
            stack.append(node.l)
        if node.r:
            stack.append(node.r)

f = Node('f')
e = Node('e')
d = Node('d')
c = Node('c', f)
b = Node('b', d, e)
a = Node('a', b, c)

print_tree(a)
invert_tree(a)
print()
print_tree(a)

# ex1tree = [None, 'a', 'b', 'c', 'd', 'e', 'f', None]
# ex1inverted = [None, 'a', 'c', 'b', None, 'f', 'e', 'd']

