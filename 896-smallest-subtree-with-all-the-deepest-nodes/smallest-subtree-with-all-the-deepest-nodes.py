# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        counter = defaultdict(int)
        def dfs(node, depth):
            nonlocal counter
            if not node:
                return
            counter[depth] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        _max, counts = -1, 0
        for k, v in counter.items():
            if k > _max:
                _max , counts = k , v
        # there are counts count with depth _max
        ans , found = None, False
        def dfs2(node, depth):
            nonlocal _max
            nonlocal ans
            nonlocal found
            if not node:
                return 0
            x = dfs2(node.left, depth + 1)
            y = dfs2(node.right, depth + 1)
            cand = x + y + (depth == _max)
            if cand == counts and not found:
                ans = node
                found = True
            return cand
        dfs2(root, 0)
        return ans