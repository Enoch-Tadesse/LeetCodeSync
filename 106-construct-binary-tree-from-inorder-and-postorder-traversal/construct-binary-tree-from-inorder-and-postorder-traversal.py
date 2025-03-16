# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder Left Node Right
        # postorder Left Right Node
        if len(postorder) == 0:
            return None
        idx = inorder.index(postorder[-1])
        node = TreeNode(val=postorder[-1])
        node.left = self.buildTree(inorder[:idx], postorder[:idx])
        node.right = self.buildTree(inorder[idx + 1:] , postorder[idx: -1])
        return node