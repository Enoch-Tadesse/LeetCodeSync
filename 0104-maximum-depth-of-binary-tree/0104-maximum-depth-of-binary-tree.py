# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(node,curr):
            nonlocal res
            if not node:
                res = max(res, curr)
                return
            depth(node.left, curr+1)
            depth(node.right, curr+1)
        depth(root, 0)
        return res
        
        # if not root:
        #     return 0
        # res = 0
        # q = deque([(root,1)])
        # while q:
        #     curr,depth = q.popleft()
        #     res = max(res,depth)
        #     if curr.left:
        #         q.append((curr.left,depth+1))
        #     if curr.right:
        #         q.append((curr.right,depth+1))
        # return res
        