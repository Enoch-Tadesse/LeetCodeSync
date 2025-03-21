# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(node, upper_sum):
            if not node:
                return 0

            right_sum = dfs(node.right, upper_sum)
            right_sum += node.val
            left_sum = dfs(node.left, right_sum + upper_sum)
            node.val = right_sum + upper_sum
            return right_sum + left_sum
            
        dfs(root, 0)
        return root