# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = self.inorder(root)
        for i in range(len(nums)- 2, -1, -1):
            nums[i].val += nums[i+1].val
        return root

    def inorder(self, root):
        if not root:
            return [TreeNode(val=0)]
        return [*self.inorder(root.left) , root, *self.inorder(root.right)]