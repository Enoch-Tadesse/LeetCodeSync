class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # if x is odd and there exist an even and odd mix in grid, NO except x == 1
        # if all grid ele are even and x is even, converge to median
        nums = []
        for row in grid:
            nums.extend(row)
        for i in range(1, len(nums)):
            if nums[i] % x != nums[i-1] % x:
                return -1
        nums.sort()
        con = len(nums) // 2
        ele = nums[con]
        counter = 0
        for num in nums:
            counter += abs(ele - num) // x
        return counter
        