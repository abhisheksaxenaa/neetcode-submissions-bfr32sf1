# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkIfGoodNode(self, node: TreeNode, maxval: int):
        if node is None:
            return
        # print(f"{node.val} vs {maxval}")
        if node.val >= maxval:
            self.goodCount += 1
        self.checkIfGoodNode(node.left, max(node.val, maxval))
        self.checkIfGoodNode(node.right, max(node.val, maxval))

    def goodNodes(self, root: TreeNode) -> int:
        # Maintain global count
        # root is always good
        # Check for left and right
        if root is None:
            return 0
        self.goodCount = 1
        self.checkIfGoodNode(root.left, root.val)
        self.checkIfGoodNode(root.right, root.val)
        return self.goodCount
        