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
        resLen = 0
        while q:
            idx , curr = q.popleft()
            if idx >= resLen:
                res.append([curr.val])
                resLen+=1
            else:
                res[idx].append(curr.val)
            if curr.left:
                q.append((idx+1, curr.left))
            if curr.right:
                q.append((idx+1, curr.right))
        return res