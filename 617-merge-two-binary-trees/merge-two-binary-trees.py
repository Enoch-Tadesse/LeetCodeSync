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
        if not root1 and not root2:
            return None
        l = root1.val if root1 else 0
        r = root2.val if root2 else 0
        mer = TreeNode(val=l+r)
        if root1 and root2:
            mer.left = self.traverse(root1.left, root2.left)
            mer.right = self.traverse( root1.right, root2.right)
        elif root1:
            mer.left = self.traverse(root1.left, None)
            mer.right = self.traverse( root1.right, None)
        else:
            mer.left = self.traverse(None, root2.left)
            mer.right = self.traverse( None, root2.right)
        return mer