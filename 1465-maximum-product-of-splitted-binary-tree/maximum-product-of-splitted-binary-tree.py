# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.MOD = 10 ** 9 + 7
        self.sum = defaultdict(int)
        self.traverse(root)

        self.res = -1
        self.helper(root, self.sum[root])
        return self.res % self.MOD
    def helper(self, root, top):
        if not root:
            return
        l = self.sum[root.left]
        self.res = max(self.res , l * (top - l))
        r = self.sum[root.right]
        self.res = max(self.res, r * (top - r))
        self.helper(root.left, top)
        self.helper(root.right, top)

    def traverse(self, root):
        if root in self.sum:
            return self.sum[root]
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.sum[root] = (root.val + left + right)
        return root.val + left + right