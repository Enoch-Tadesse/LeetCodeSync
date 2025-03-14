# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.helper(root)
        return self.res
    def helper(self, root):
        if not root or not self.res:
            return (float("inf"), float("-inf") ) # left and right
        l_min , l_max = self.helper(root.left)
        r_min , r_max = self.helper(root.right)

        self.res = self.res and (root.val > l_max if root.left else True)
        self.res = self.res and (root.val < r_min if root.right else True)

        print(f"{root.val=} min={min(root.val, l_min , r_min)} max={max(root.val, l_max, r_max)} {self.res=}")
        return (min(root.val, l_min , r_min) , max(root.val, l_max, r_max))