# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        self.traverse(root, 0)
        return max(self.ans, 0)
    def traverse(self, root, curr):
        if not root: # returns the (current sum, min , max, isvalidBST)
            return (0 , float("inf"), float("-inf"), True)
        
        left , l_min, l_max, l_valid = self.traverse(root.left, curr)
        right , r_min , r_max , r_valid = self.traverse(root.right, curr)
        valid = False
        # print(f"{root.val=} {l_min=} {l_max=} {r_min=} {r_max=}")
        if l_valid and r_valid and l_max < root.val and r_min > root.val:
            # print("valid")
            valid = True
            self.ans = max(self.ans , left + right + root.val)
        l = min(l_min, root.val)
        r = max(r_max, root.val)
        valid = l_valid and r_valid and valid

        return (left + right + root.val, l , r, valid)