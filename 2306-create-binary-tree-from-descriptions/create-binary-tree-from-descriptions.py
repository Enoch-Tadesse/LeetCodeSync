# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        cand = set()
        for a, b, t in descriptions:
            if a not in nodes:
                nodes[a] = TreeNode(val=a)
            if b not in nodes:
                nodes[b] = TreeNode(val=b)
            if not t:
                nodes[a].right = nodes[b]
            else:
                nodes[a].left = nodes[b]
            cand.add(b)
        for k, v in nodes.items():
            if k not in cand:
                return v
        
        