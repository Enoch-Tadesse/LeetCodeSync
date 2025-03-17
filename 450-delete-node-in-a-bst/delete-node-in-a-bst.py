# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        dummy = TreeNode(float("inf"))
        dummy.left = root
        self.delete(dummy, key)
        return dummy.left
        
    def delete(self, root, key):
        if not root:
            return
        if root.left and root.left.val == key:
            if root.left.left:
                root.left.right = self.insert(root.left.right, root.left.left)
            root.left = root.left.right
            return
        if root.right and root.right.val == key:
            if root.right.left:
                root.right.right = self.insert(root.right.right, root.right.left)
            root.right = root.right.right
            return
        if key < root.val:
            self.delete(root.left, key)
        if key > root.val:
            self.delete(root.right, key)
        
    def insert(self, parent, root):
        if not parent:
            return root
        if root.val > parent.val:
            parent.right = self.insert(parent.right, root)
        else:
            parent.left = self.insert(parent.left, root)
        return parent