# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        self.helper(root, p.val, q.val)
        return self.res
    def helper(self, root, p, q):
        if not root:
            return False , False

        lpf, lqf = self.helper(root.left, p, q)
        rpf, rqf = self.helper(root.right, p, q)

        pfound = lpf or rpf or root.val == p
        qfound = lqf or rqf or root.val == q

        if pfound and qfound:
            if not self.res:
                self.res = root
            return True, True
        
        return pfound, qfound

        