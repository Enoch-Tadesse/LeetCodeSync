# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # one node tells, if you took me and left side this is what you get
        # if you take me and the right side this is what you get
        self.ans = float("-inf")
        self.helper(root)
        return self.ans
    def helper(self, root):
        if not root:
            return 0
        lsum = max(self.helper(root.left), 0)
        rsum = max(self.helper(root.right), 0)
        self.ans = max(self.ans, lsum + rsum + root.val)
        return max(lsum + root.val , rsum + root.val)
