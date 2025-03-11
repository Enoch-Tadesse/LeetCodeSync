class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        special = {'a', 'b', 'c'}
        counter = 0
        curr = defaultdict(int)
        left = 0
        for right in range(len(s)):
            curr[s[right]] += 1
            while len(curr) == len(special):
                counter += n - right
                curr[s[left]] -= 1
                if curr[s[left]] == 0:
                    del curr[s[left]]
                left += 1
        return counter