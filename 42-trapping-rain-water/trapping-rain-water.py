class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left = height[l]
        right = height[r]
        vol = 0
        while l < r:
            if left <= right:
                l+=1
                left = max(left, height[l])
                vol += left - height[l]
            else:
                r-=1
                right = max(right, height[r])
                vol+= right - height[r]
        return vol
