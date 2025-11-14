# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = 0
        def dfs(node):
            nonlocal counter
            if not node:
                return {}
            out = dict()
            l = dfs(node.left)
            r = dfs(node.right)
            for k , v in l.items():
                out[k + node.val] = out.get(k + node.val, 0) + v
            for k , v in r.items():
                out[k + node.val] = out.get(k + node.val, 0) + v
            out[node.val] = out.get(node.val, 0) + 1
            if targetSum in out:
                counter += out[targetSum]
            return out

        dfs(root)
        return counter