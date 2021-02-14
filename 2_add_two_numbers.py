class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LList:
    def __init__(self):
        self.root = None
        self.tail = None

    def add_node(self, val: int):
        node = ListNode(val)

        if self.root is None:
            self.root = node
        else:
            self.tail.next = node
        self.tail = node

    def fetch_root(self):
        return self.root


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = LList()
        carry = 0

        while l1 is not None and l2 is not None:
            s, carry = self.add_digits(l1, l2, carry)
            res.add_node(s)

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            s, carry = self.add_digits(l1, ListNode(0), carry)
            res.add_node(s)

            l1 = l1.next

        while l2 is not None:
            s, carry = self.add_digits(l2, ListNode(0), carry)
            res.add_node(s)

            l2 = l2.next

        if carry:
            res.add_node(1)

        return res.fetch_root()

    def add_digits(self, d1: ListNode, d2: ListNode, carry: int = 0):
        s = d1.val + d2.val + carry

        carry = s // 10
        s = s % 10

        return s, carry
