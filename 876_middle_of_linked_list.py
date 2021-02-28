# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ptr, fptr = head, head

        while fptr is not None and fptr.next is not None:
            ptr = ptr.next
            fptr = fptr.next.next

        return ptr