# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        temp = []
        ans = []
        def dfs(node, curr):
            if not node:
                return
            temp.append(node.val)
            if curr - node.val == 0 and not node.left and not node.right:
                ans.append(temp[:])
            dfs(node.left, curr - node.val)
            dfs(node.right, curr - node.val)
            temp.pop()
        dfs(root, targetSum)
        return ans