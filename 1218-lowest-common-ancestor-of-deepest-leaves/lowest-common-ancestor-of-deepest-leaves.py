# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.depths = defaultdict(int)
        self.getDepth(root)
        self.depth = max(self.depths.values())
        self.ans = None
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root:
            return
        l = self.depths[root.left]
        r = self.depths[root.right]
        if l > r:
            if self.helper(root.left):
                return True
        elif r > l:
            if self.helper(root.right):
                return True
        else:
            self.ans = root
            return True


    def getDepth(self,root):
        if not root:
            return 0
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)

        self.depths[root] = 1 + max(l , r)
        return self.depths[root]
                