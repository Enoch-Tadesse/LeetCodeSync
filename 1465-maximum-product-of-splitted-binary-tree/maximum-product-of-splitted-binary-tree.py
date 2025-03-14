# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        self.total = self.traverse(root) # get the total sum

        self.res = -1
        self.helper(root)
        return self.res % MOD

    def traverse(self, root):
        if not root:
            return 0
        return root.val + self.traverse(root.left) + self.traverse(root.right)
    
    def helper(self, root):
        if not root:
            return 0
        # get the left and right sum
        left = self.helper(root.left)
        right = self.helper(root.right)
        # try both update bisecting left or right
        self.res = max(self.res, left * (self.total - left))
        self.res = max(self.res, right * (self.total - right))

        return root.val + left + right