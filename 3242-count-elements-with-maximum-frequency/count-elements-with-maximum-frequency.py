class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        _max = max(counts.values())
        ans = list(counts.values()).count(_max)
        return ans * _max
        
                