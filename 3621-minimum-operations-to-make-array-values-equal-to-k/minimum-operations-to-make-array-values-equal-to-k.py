class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = min(nums)
        if x < k:
            return -1
        bigs = set()
        for num in nums:
            if num > k:
                bigs.add(num)
        return len(bigs)