"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        levels = dict()
        self.__level_order_traversal(root, 0, levels)

        for level in levels.values():
            self.__connect_nodes_per_level(level)

        return levels[0][0]

    def __level_order_traversal(self, root: 'Node', level: int, traversal: dict):
        if root is None:
            return

        if level not in traversal:
            traversal[level] = list()
        traversal[level].append(root)

        self.__level_order_traversal(root.left, level + 1, traversal)
        self.__level_order_traversal(root.right, level + 1, traversal)

    def __connect_nodes_per_level(self, nodes_per_level: list):
        prev = None

        for node in nodes_per_level:
            if prev is not None:
                prev.next = node

            prev = node

        nodes_per_level[-1].next = None
