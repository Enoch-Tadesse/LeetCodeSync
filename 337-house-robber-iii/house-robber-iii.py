# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # rob , not rob
        @cache
        def dp(node):
            if not node:
                return 0
            # not rob
            skip = dp(node.left) + dp(node.right)
            # rob
            rob = node.val
            if node.left:
                rob += dp(node.left.left)
                rob += dp(node.left.right)
            if node.right:
                rob += dp(node.right.left)
                rob += dp(node.right.right)
            return max(skip, rob)
        return dp(root)
