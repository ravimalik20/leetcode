# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        curr, prev, i = head, None, 0
        while curr is not None:
            i += 1

            if i % 2 == 0:
                self._swap(prev, curr)

            prev, curr = curr, curr.next

        return head

    def _swap(self, node1: ListNode, node2: ListNode):
        node1.val, node2.val = node2.val, node1.val
