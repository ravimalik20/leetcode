# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return 1 + self._traverse_good_nodes(root.left, root) + self._traverse_good_nodes(root.right, root)

    def _traverse_good_nodes(self, root: TreeNode, last_known_good_node: TreeNode):
        if root is None:
            return 0

        if root.val >= last_known_good_node.val:
            return 1 + self._traverse_good_nodes(root.left, root) + \
                   self._traverse_good_nodes(root.right, root)
        else:
            return self._traverse_good_nodes(root.left, last_known_good_node) + \
                   self._traverse_good_nodes(root.right, last_known_good_node)
