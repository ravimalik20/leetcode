from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        traversal = self._level_order_traversal(root, 0, dict())

        return self._prepare_output(traversal)

    def _level_order_traversal(self, root: TreeNode, level: int, traversal: dict) -> dict:
        if root == None:
            return traversal

        if level not in traversal:
            traversal[level] = list()
        traversal[level].append(root.val)

        self._level_order_traversal(root.left, level + 1, traversal)
        self._level_order_traversal(root.right, level + 1, traversal)

        return traversal

    def _prepare_output(self, traversal: dict) -> List[List[int]]:
        depth = len(traversal)
        out = []

        for i in range(depth - 1, -1, -1):
            out.append(traversal[i])

        return out
