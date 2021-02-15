from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LList:
    def __init__(self):
        self.root = None
        self.tail = None

    def add(self, val):
        node = ListNode(val)

        if self.root is None:
            self.root = node
        else:
            self.tail.next = node
        self.tail = node


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]

        mid = n // 2

        l1 = self.mergeKLists(lists[:mid])
        l2 = self.mergeKLists(lists[mid:])

        return self.__merge_two_lists(l1, l2)

    def __merge_two_lists(self, list1: ListNode, list2: ListNode):
        merged_list = LList()

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                merged_list.add(list1.val)
                list1 = list1.next
            else:
                merged_list.add(list2.val)
                list2 = list2.next

        while list1 is not None:
            merged_list.add(list1.val)
            list1 = list1.next

        while list2 is not None:
            merged_list.add(list2.val)
            list2 = list2.next

        return merged_list.root
