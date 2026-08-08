# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1,2,3,4

4.3.2.1


'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        curr = head
        prev = None
        count = 0
        while curr:
            stack.append(curr)
            curr = curr.next

        while count != n:
            curr = stack.pop()
            count += 1

        # either this is at last
        # either this is at first, prev will be none
        # either this is in middle
        if stack:
            prev = stack.pop()
        if not prev:
            return curr.next
        prev.next = curr.next
        curr.next = None
        return head