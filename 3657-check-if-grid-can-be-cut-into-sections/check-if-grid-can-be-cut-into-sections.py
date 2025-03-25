class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def solve(nums):
            nums.sort()
            gaps = 0
            _max = nums[0][1]
            for i in range(1, len(nums)):
                if nums[i][0] >= _max:
                    gaps += 1
                _max = max(nums[i][1], _max)
            # print(gaps, nums)
            return gaps > 1
        hori = []
        ver = []
        for x1, y1, x2, y2 in rectangles:
            hori.append((y1, y2))
            ver.append((x1, x2))
        return solve(hori) or solve(ver)
