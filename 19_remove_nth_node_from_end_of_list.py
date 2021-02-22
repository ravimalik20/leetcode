# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = self.__len_list(head)
        i = l - n

        prev, curr = None, head

        while i > 0:
            prev = curr
            curr = curr.next

            i -= 1

        if prev is None:
            head = head.next
        else:
            prev.next = curr.next

        return head

    def __len_list(self, head: ListNode):
        l = 0
        while head is not None:
            l += 1

            head = head.next

        return l
