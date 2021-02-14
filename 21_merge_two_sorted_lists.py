# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LList:
    def __init__(self):
        self.root = None
        self.tail = None

    def add_node(self, node: ListNode):
        if self.root is None:
            self.root = node
        else:
            self.tail.next = node

        self.tail = node


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ml = LList()

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                ml.add_node(l1)
                l1 = l1.next
            else:
                ml.add_node(l2)
                l2 = l2.next

        while l1 is not None:
            ml.add_node(l1)
            l1 = l1.next

        while l2 is not None:
            ml.add_node(l2)
            l2 = l2.next

        return ml.root
