# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left = self.solve(root.left)
        right = self.solve(root.right)

        result = max(max(left, right) + root.val, root.val)
        self.max_val = max(self.max_val, result, left + right + root.val)

        return result

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return root.val
        self.max_val = float('-inf')
        self.solve(root)
        return self.max_val