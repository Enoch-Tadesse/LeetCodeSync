# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        self.helper(root, float("inf"), float("-inf"))
        return self.res
    def helper(self, root, _min, _max):
        if not root:
            return
        if _min != float("inf"):
            self.res = max(self.res, abs(_min - root.val))
        if _max != float("-inf"):
            self.res = max(self.res, abs(_max - root.val))
        self.helper(root.left, min(_min, root.val), max(_max, root.val))
        self.helper(root.right, min(_min , root.val) , max(_max , root.val))