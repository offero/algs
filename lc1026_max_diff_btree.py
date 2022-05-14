import json
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def ldd(val, node):
    if node is None:
        return 0
    v1 = abs(val - node.val)
    v2 = ldd(val, node.left)
    v3 = ldd(val, node.right)
    return max(v1, v2, v3)

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        v1 = ldd(root.val, root.left)
        v2 = ldd(root.val, root.right)
        v3 = self.maxAncestorDiff(root.left)
        v4 = self.maxAncestorDiff(root.right)
        return max(v1, v2, v3, v4)


a = TreeNode(8,
        TreeNode(3,
            TreeNode(1),
            TreeNode(6,
                TreeNode(4),
                TreeNode(7)
            )
        ),
        TreeNode(10,
            None,
            TreeNode(14,
                TreeNode(13),
                None
            )
        )
    )

# sol = Solution()
# print(sol.maxAncestorDiff(a))


def treeFromList(values, i=0):
    if values[i] is None:
        return None
    node = TreeNode(values[i])
    left_idx = (i+1)*2
    right_idx = (i+1)*2 + 1
    if left_idx-1 < len(values):
        node.left = treeFromList(values, i=left_idx-1)
    if right_idx-1 < len(values):
        node.right = treeFromList(values, i=right_idx-1)
    return node


# vals = json.loads("[8,3,10,1,6,null,14,null,null,4,7,13]")
vals = json.load(open('./lc1026_test_case.json'))
print(Solution().maxAncestorDiff(treeFromList(vals)))

