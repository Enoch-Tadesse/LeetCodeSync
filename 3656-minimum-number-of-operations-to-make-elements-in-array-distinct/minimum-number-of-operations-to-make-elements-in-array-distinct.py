class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        _max = -3
        for i , num in enumerate(nums):
            if num in seen:
                _max = max(_max, seen[num])       
            seen[num] = i
        return _max // 3 + 1
            