# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        result = ListNode(0)
        current = result
        while list1 and list2:
            val1 = list1.val
            val2 = list2.val
            if val1 < val2:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return result.next

    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        
        mid = l + (r - l) //2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)

        return self.merge_two_lists(left, right)
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divide(lists, 0, len(lists) - 1)
        