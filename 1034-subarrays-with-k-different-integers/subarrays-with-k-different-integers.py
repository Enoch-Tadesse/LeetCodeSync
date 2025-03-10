class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atLeast(nums, k) - self.atLeast(nums, k+1)
        
    def atLeast(self, nums, k):
        seen = defaultdict(int)
        counter = 0
        left = 0
        for right in range(len(nums)):
            seen[nums[right]] += 1
            while len(seen) >= k:
                counter += len(nums) - right
                seen[nums[left]] -= 1
                if seen[nums[left]] == 0:
                    del seen[nums[left]]
                left += 1
        return counter