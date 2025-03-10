class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        self.vowels = set(['a' , 'e', 'i', 'o', 'u'])
        return self.atLeast(word, k) - self.atLeast(word, k+1)

    def atLeast (self, word, k):
        counter = left  = counts = 0
        n = len(word)
        curr = defaultdict(int)
        for right in range(n):
            if word[right] not in self.vowels:
                counts += 1
            else:
                curr[word[right]] += 1
            while right < n and counts >= k and len(curr) == len(self.vowels):
                counter += n - right
                if word[left] not in self.vowels:
                    counts -= 1
                else:
                    curr[word[left]] -= 1
                    if curr[word[left]] == 0:
                        del curr[word[left]]
                left += 1
        return counter
            