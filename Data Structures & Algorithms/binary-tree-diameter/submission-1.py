# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calculateDiameter(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        # print(root.val)
        left = self.calculateDiameter(root.left)
        right = self.calculateDiameter(root.right)
        # print(f'Left @ {root.val} : {left}')
        # print(f'Right @ {root.val} : {right}')
        self.diameter = max(self.diameter, left + right, left, right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return 0
        self.diameter = 0
        self.calculateDiameter(root)
        return self.diameter