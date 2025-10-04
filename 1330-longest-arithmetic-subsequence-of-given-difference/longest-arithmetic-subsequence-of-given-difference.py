class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        last = defaultdict(int)
        for num in arr:
            last[num] = max(1 + last[num - difference], last[num])
        return max(last.values())