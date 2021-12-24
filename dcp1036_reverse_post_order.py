"""
DCP #1036

Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the
tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8
"""

class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def post_order(r):
    if r.left:
        yield from post_order(r.left)
    if r.right:
        yield from post_order(r.right)
    yield r.value


def reverse_po(po):
    t = TreeNode(po[-1])

    i = len(po) - 2
    while i >= 0:
        value = po[i]
        print(value, t.value)

        if value >= t.value:
            print('set', value, 'to right of', t.value)
            t.right = TreeNode(value, parent=t)
            t = t.right
            i -= 1
            continue

        # traverse up if there exists a parent
        # and the parents value is less then our value
        # and the parent value is less than the current value
        if t.parent and t.parent.value < t.value and value < t.parent.value:
            print('up')
            t = t.parent
            continue

        if value < t.value:
            print('set', value, 'to left of', t.value)
            t.left = TreeNode(value, parent=t)
            t = t.left
            i -= 1
            continue

    while t.parent:
        t = t.parent

    return t


def main():
    tree_ex = \
        TreeNode(5,
            TreeNode(3,
                TreeNode(2),
                TreeNode(4)
            ),
            TreeNode(7,
                None,
                TreeNode(8)
            )
        )

    print(list(post_order(tree_ex)))

    po_ex1 = [2, 4, 3, 8, 7, 5]
    print(list(post_order(reverse_po(po_ex1))))


if __name__ == "__main__":
    main()
