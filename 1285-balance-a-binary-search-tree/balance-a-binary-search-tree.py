# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = self.inorder(root)
        root = self.construct(nums, 0, len(nums))
        return root
        
    def construct(self, nums, left, right):
        if left == right:
            return None
        mid = (right + left) // 2
        root = TreeNode(val=nums[mid])
        root.left = self.construct(nums, left, mid)
        root.right = self.construct(nums, mid + 1, right)
        return root

    def inorder(self, root):
        if not root:
            return []
        return [*self.inorder(root.left) , root.val, *self.inorder(root.right)]