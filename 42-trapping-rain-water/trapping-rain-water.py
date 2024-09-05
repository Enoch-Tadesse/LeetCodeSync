class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        vol = 0
        leftHigh = height[l]
        rightHigh = height[r]
        while l < r:
            if leftHigh < rightHigh:
                l+=1
                leftHigh = max(leftHigh, height[l])
                vol += leftHigh - height[l]
            else:
                r-=1
                rightHigh = max(rightHigh, height[r])
                vol += rightHigh - height[r]
        return vol