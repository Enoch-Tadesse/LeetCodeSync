# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 0
        self.helper(root, 0)
        return self.ans

    def helper(self, root, curr):
        if not root.left and not root.right:
            self.ans += curr * 10 + root.val
            return
        if root.left:
            self.helper(root.left, curr * 10 + root.val)
        if root.right:
            self.helper(root.right, curr * 10 + root.val)