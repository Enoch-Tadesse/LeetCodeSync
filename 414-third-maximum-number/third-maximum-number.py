class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f = s = t = float("-inf")
        seen = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            if num > f:
                f, s, t = num, f, s
            elif num > s:
                s, t = num, s
            elif num > t:
                t = num
        if t != float("-inf"):
            return t
        return max(f, s, t)