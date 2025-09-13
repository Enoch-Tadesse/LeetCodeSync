class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e','i','o','u'}
        vcounts = defaultdict(int)
        ncounts = defaultdict(int)
        for w in s:
            if w in vowels:
                vcounts[w] += 1
            else:
                ncounts[w] += 1
        vcounts['dummy'] = 0
        ncounts['dummy'] = 0
        return max(vcounts.values()) + max(ncounts.values())