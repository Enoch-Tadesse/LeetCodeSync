# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(0,root)])
        res = []
        while q:
            idx , curr = q.popleft()
            if idx >= len(res):
                res.append([curr.val])
            else:
                res[idx].append(curr.val)
            if curr.left:
                q.append((idx+1, curr.left))
            if curr.right:
                q.append((idx+1, curr.right))
        return res