# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
A(n) -> B(f) -> C -> D
p = None

itr 1
A(p) B(n) -> C(f) -> D

itr 2
A <- B(p) C(n) -> D(f)

itr 3
A <- B <- C(p) D(n)
f = None
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node: Optional[ListNode] = head
        prev: Optional[ListNode] = None
        if head is None or head.next is None:
            return head
        fast: Optional[ListNode] = head.next

        while fast is not None:
            node.next = prev
            prev = node
            node = fast
            fast = fast.next

        node.next = prev

        return node