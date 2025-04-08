class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = [-1] * 101
        _max = -3
        for i , num in enumerate(nums):
            if seen[num] != -1:
                _max = max(_max, seen[num])       
            seen[num] = i
        return _max // 3 + 1
            