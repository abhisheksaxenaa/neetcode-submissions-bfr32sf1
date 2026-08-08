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
        stack = []
        slow = head
        fast = None
        if head is None or head.next is None or head.next.next is None:
            return

        while slow is not None:
            stack.append(slow)
            slow = slow.next
        current = head
        ahead = head.next
        while len(stack):
            node = stack.pop()
            if current == node:
                current.next = None
                return
            if ahead == node:
                ahead.next = None
                return
            current.next = node
            node.next = ahead
            current = ahead
            ahead = ahead.next


