# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        q = deque([root])
        depth = 0
        while q:
            k = len(q)
            for i in range(k):
                if q[i].right or q[i].left:
                    q.append(q[i].left)
                    q.append(q[i].right)
            if depth & 1:
                l , r = 0, k - 1
                while l < r:
                    q[l].val , q[r].val = q[r].val , q[l].val
                    l , r = l + 1 , r - 1
            for i in range(k):
                q.popleft()
            depth += 1
        return root
