from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = list()

        self._inorder_traversal_list(root, output)

        return output

    def _inorder_traversal_list(self, root: TreeNode, output: list):
        if root is None:
            return root

        self._inorder_traversal_list(root.left, output)
        output.append(root.val)
        self._inorder_traversal_list(root.right, output)
