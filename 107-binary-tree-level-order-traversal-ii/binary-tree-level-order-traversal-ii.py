# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            temp = []
            k = len(q)
            for i in range(k):
                parent = q.popleft()
                if parent.left:
                    q.append(parent.left)
                if parent.right:
                    q.append(parent.right)
                temp.append(parent.val)
            result.append(temp)
        return result[::-1]