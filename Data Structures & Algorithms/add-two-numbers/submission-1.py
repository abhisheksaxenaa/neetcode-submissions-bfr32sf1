# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode(0)
        current = result_head
        carry = 0
        c1 = l1
        c2 = l2

        while c1 or c2 or carry:
            digit1 = c1.val if c1 else 0
            digit2 = c2.val if c2 else 0
            digit_sum = digit1 + digit2 + carry
            carry = digit_sum // 10
            current.next = ListNode(digit_sum % 10)
            current = current.next

            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next

        return result_head.next