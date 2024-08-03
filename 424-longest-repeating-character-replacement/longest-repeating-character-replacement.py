class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        max_count = 0
        result = 0
        counter = defaultdict(int)
        for r in range(len(s)):
            counter[s[r]]+=1
            max_count = max(max_count, counter[s[r]])
            if (r- l + 1) - max_count > k:
                counter[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result