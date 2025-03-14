# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        q = deque([root])
        while q:
            _curr = float("-inf")
            k = len(q)
            for i in range(k):
                parent = q.popleft()
                _curr = max(_curr, parent.val)
                if parent.left:
                    q.append(parent.left)
                if parent.right:
                    q.append(parent.right)
            output.append(_curr)
        return output