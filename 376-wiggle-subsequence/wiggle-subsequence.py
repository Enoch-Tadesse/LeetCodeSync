class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return len(set(nums))
        curr = 0
        counter = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if curr != -1:
                    counter += 1
                    curr = -1
            elif nums[i] > nums[i - 1]:
                if curr != 1:
                    counter += 1
                    curr = 1
        return counter + 1