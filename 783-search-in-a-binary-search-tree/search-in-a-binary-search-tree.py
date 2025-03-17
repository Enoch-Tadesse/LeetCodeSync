# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.helper(root, val)
    def helper(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.helper(root.right, val)
        else:
            return self.helper(root.left, val)