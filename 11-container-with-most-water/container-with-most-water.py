class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        res = float("-inf")
        while i < j:
            left = height[i]
            right = height[j]
            curr = (j-i) * min(left, right)
            res = max(res,curr)
            if left <= right:
                i+=1
            else:
                j-=1
        return res