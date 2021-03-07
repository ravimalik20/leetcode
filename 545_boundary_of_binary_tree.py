from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        lhs_boundary = self.__lhs_boundary_excluding_leaf(root.left)
        rhs_boundary = self.__rhs_boundary_excluding_leaf(root.right)

        print(lhs_boundary)
        print(rhs_boundary)

        leaves_boundary = list()
        self.__leaf_nodes(root, leaves_boundary)

        return [root.val] + lhs_boundary + leaves_boundary + rhs_boundary[::-1]

    def __lhs_boundary_excluding_leaf(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = []
        while root.left is not None or root.right is not None:
            res.append(root.val)

            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                break

        return res

    def __rhs_boundary_excluding_leaf(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = []
        while root.left is not None or root.right is not None:
            res.append(root.val)

            if root.right:
                root = root.right
            elif root.left:
                root = root.left
            else:
                break

        return res

    def __leaf_nodes(self, root: TreeNode, leaves: List[int]):
        if root is None:
            return None

        if root.left is None and root.right is None:
            leaves.append(root.val)
        else:
            self.__leaf_nodes(root.left, leaves)
            self.__leaf_nodes(root.right, leaves)
