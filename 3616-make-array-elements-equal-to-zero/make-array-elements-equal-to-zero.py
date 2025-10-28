class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # if they are equal, moving right and left are possible
        # if the right or left dominates just by one, only one is possible
        counter = 0
        total = sum(nums)
        curr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                curr += nums[i]
                continue
            right = total - curr
            if right == curr:
                counter += 2
            elif abs(right - curr) == 1:
                counter += 1
        return counter