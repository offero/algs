'''
DCP #1418

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
'''

class Node:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent

def binary_search(root, value):
    if root == None:
        return False

    if value == root.value:
        return root

    if value < root.value:
        return binary_search(root.left, value)

    return binary_search(root.right, value)

def find_greater_child(node, value):
    while node.right:
        node = node.right
        if node.value > value:
            return node

def inorder_successor(node, value):
    succ = find_greater_child(node, value)
    if not succ and node.parent.value > value:
        return node.parent
    return succ

def find_inorder_successor(root, value):
    # first, find value using binary search
    # second, find inorder successor
    node = binary_search(root, value)
    # print('found node', node.value)
    succ = inorder_successor(node, value)
    # print('found succ', succ and succ.value)
    return succ and succ.value


N10 = Node(10)
N5 = Node(5)
N30 = Node(30)
N22 = Node(22)
N35 = Node(35)

N10.left = N5
N10.parent = None
N5.parent = N10
N10.right = N30
N30.parent = N10
N30.left = N22
N22.parent = N30
N30.right = N35
N35.parent = N30

def main():
    print(find_inorder_successor(N10, 10))
    print(find_inorder_successor(N10, 5))
    print(find_inorder_successor(N10, 22))
    print(find_inorder_successor(N10, 30))
    print(find_inorder_successor(N10, 35))

if __name__ == '__main__':
    main()
