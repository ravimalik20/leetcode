class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        sorted_nodes = list()
        self.__inorder_traversal_bst(root, sorted_nodes)

        return self.__prepare_doubly_linked_list(sorted_nodes)

    def __inorder_traversal_bst(self, root: 'Node', traversal: list):
        if root is None:
            return

        self.__inorder_traversal_bst(root.left, traversal)

        traversal.append(root)

        self.__inorder_traversal_bst(root.right, traversal)

    def __prepare_doubly_linked_list(self, sorted_nodes: list) -> 'Node':
        prev = sorted_nodes[-1]

        for i in range(0, len(sorted_nodes)):
            curr = sorted_nodes[i]

            prev.right = curr
            curr.left = prev

            prev = curr

        return sorted_nodes[0]
