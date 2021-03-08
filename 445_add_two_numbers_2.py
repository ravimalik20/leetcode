# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LList:
    def __init__(self):
        self.root = None
        self.tail = None

    def push(self, val: int):
        node = ListNode(val)

        if self.root is None:
            self.root = node
        else:
            self.tail.next = node
        self.tail = node


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.__reverse_list(l1)
        l2 = self.__reverse_list(l2)

        list_sum = self.__add_lists(l1, l2)

        return self.__reverse_list(list_sum)

    def __reverse_list(self, l: ListNode) -> ListNode:
        prev, curr = None, l

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr

            curr = nxt

        return prev

    def __add_list_nodes(self, l1: ListNode, l2: ListNode, carry=0):
        s = l1.val + l2.val + carry

        return s % 10, s // 10

    def __add_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        list_sum = LList()

        while l1 is not None and l2 is not None:
            s, carry = self.__add_list_nodes(l1, l2, carry)
            list_sum.push(s)

            l1, l2 = l1.next, l2.next

        while l1 is not None:
            s, carry = self.__add_list_nodes(l1, ListNode(0), carry)
            list_sum.push(s)

            l1 = l1.next

        while l2 is not None:
            s, carry = self.__add_list_nodes(l2, ListNode(0), carry)
            list_sum.push(s)

            l2 = l2.next

        if carry:
            list_sum.push(carry)

        return list_sum.root
