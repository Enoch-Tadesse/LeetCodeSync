class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        vol = 0
        while i != j:
            min_height = min(height[i], height[j])
            vol_temp = min_height * (j-i)
            if vol_temp > vol:
                vol = vol_temp
            if min_height == height[i]:
                i+=1
            else:
                j-=1
        return vol