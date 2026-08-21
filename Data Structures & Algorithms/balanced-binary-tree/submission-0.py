# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def count_node(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = self.count_node(node.left)
        right = self.count_node(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left-right) > 1:
            return -1
        return max(left + 1, right + 1)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check = self.count_node(root)
        return check != -1