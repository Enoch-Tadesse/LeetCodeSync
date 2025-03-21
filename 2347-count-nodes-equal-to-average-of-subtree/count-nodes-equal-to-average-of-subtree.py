# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.counter = 0
        self.helper(root, 0)
        return self.counter
    def helper(self,root, sum):
        if not root:
            return (0, 0)
        left , l_count = self.helper(root.left, root.val + sum)
        right , r_count = self.helper(root.right, root.val + sum)
        if (left + right + root.val) // (l_count + r_count + 1) == root.val:
            self.counter += 1 
        return (left + right + root.val, l_count + r_count + 1)