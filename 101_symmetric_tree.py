# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self._symmetric(root, root)

    def _symmetric(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        if p.val != q.val:
            return False
        else:
            return self._symmetric(p.left, q.right) and self._symmetric(p.right, q.left)
