# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)
    def helper(self, root, p , q):
        if root.val >= p.val and root.val <= q.val:
            return root
        if root.val < p.val and root.val < q.val:
            return self.helper(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.helper(root.left, p, q)
        return root