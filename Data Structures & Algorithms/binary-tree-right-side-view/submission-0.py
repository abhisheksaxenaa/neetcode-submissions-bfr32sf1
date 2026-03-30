# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recordRightSidePerLevel(self, node: Optional[TreeNode], level: int):
        if node is None:
            return
        if node is not None:
            if len(self.output) <= level:
                self.output.append(node.val)
        self.recordRightSidePerLevel(node.right, level+1)
        self.recordRightSidePerLevel(node.left, level+1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.output = []
        if root is None:
            return self.output
        self.recordRightSidePerLevel(root, 0)
        return self.output