# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        counter = defaultdict(int)
        def dfs(node):
            nonlocal counter
            if not node:
                return 0
            cand = node.val + dfs(node.left) + dfs(node.right)
            counter[cand] += 1
            return cand
        dfs(root)
        ans = []
        _max = max(counter.values())
        for k, v in counter.items():
            if v == _max:
                ans.append(k)
        return ans