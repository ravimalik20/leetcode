# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        ptr, fptr = head, head.next

        while fptr is not None and fptr.next is not None and ptr != fptr:
            ptr = ptr.next
            fptr = fptr.next.next

        return ptr == fptr