# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return TreeNode(val)
            if node.val > val:
                node.right = helper(node.right)
                return node
            new_node = TreeNode(val)
            new_node.left = node
            return new_node
        return helper(root)