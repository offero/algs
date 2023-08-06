from __future__ import annotations
from dataclasses import dataclass

'''
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
'''
'''
Ideas:
    1. DFS with from-list
    2. Recursion with backtracking
'''



def binary_tree_paths(root):
    fromlist = {}
    stack = [root]
    solutions = []
    while stack:
        node = stack.pop()

        if node.left is not None:
            fromlist[node.left.val] = node.val
            stack.append(node.left)

        if node.right is not None:
            fromlist[node.right.val] = node.val
            stack.append(node.right)

        if node.left is None and node.right is None:
            # traverse fromlist back to root
            val = node.val
            sol = []
            while True:
                sol.append(val)
                if val not in fromlist:
                    break
                val = fromlist[val]
            solutions.append(list(reversed(sol)))
    return solutions


@dataclass
class Node:
    val: int
    left: Node
    right: Node


ex1 = Node(1,
        Node(2, None, None),
        Node(3,
             Node(4, None, None),
             Node(5, None, None),
        )
    )

print(binary_tree_paths(ex1))
