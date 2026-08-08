# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
0s -> 1s -> 2sf -> 3s -> 4fs -> 5 -> 6f

stack = []

0 -> 6 -> 1 -> 5 -> 2 -> 4 -> 3c
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = None
        if head is None or head.next is None or head.next.next is None:
            return
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse link list from mid
        current = slow.next
        prev = slow.next = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # merge two link list
        start = head
        merge = prev
        while merge:
            temp1 = start.next
            temp2 = merge.next
            start.next = merge
            merge.next = temp1
            start = temp1
            merge = temp2
