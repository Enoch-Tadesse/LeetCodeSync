# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        q = deque([root])
        depth = 0
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
            if depth & 1:
                output.append(temp[::-1])
            else:
                output.append(temp)
            depth += 1
        return output

