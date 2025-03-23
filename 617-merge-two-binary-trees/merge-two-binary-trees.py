# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.traverse(root1, root2)
    def traverse(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        mer = TreeNode(val=root1.val + root2.val)
        mer.left = self.traverse(root1.left, root2.left)
        mer.right = self.traverse( root1.right, root2.right)
        return mer