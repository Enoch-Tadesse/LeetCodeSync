class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        size = 2 * k + 1
        if (len(nums) < size):
            return [-1] * len(nums)
        total = 0

        output = [-1] * len(nums)
        l = 0
        for r in range(len(nums)):
            if r - l + 1 < size:
                total += nums[r]
                continue
            total += nums[r]
            output[l + k] = total // size
            total -= nums[l]
            l += 1
        return output