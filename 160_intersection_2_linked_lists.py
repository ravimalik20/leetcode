# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        index = self._prepare_index(headA)

        while headB is not None:
            if headB in index:
                return headB

            headB = headB.next

        return None

    def _prepare_index(self, head: ListNode):
        index = set()

        while head is not None:
            index.add(head)
            head = head.next

        return index