# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def traverse(node):
            if not node:
                return
            res[0] = max(res[0],maxDepth(node.left) + maxDepth(node.right))
            traverse(node.left)
            traverse(node.right)
        @lru_cache
        def maxDepth(node):
            if not node:
                return 0
            return max(maxDepth(node.left),maxDepth(node.right)) + 1
        traverse(root)
        return res[0]