# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        last = dummy
        prev = dummy
        current = head
        count = 1
        while current:
            # print(current.val, count)
            if count != k:
                count += 1
                current = current.next
                continue
            count = 0
            current = last.next
            temp = None
            # reverse the current section
            while count < k:
                count += 1
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            # reset last pointer
            current = last.next
            current.next = temp
            last.next = prev
            last = current
            current = current.next
            count = 1


        return dummy.next



