class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        seen = {w[::-1] : i for i , w in enumerate(words)}
        ans = []
        for i , w in enumerate(words):
            for j in range(len(w) + 1):
                pre , suf = w[:j] , w[j:]
                if pre == pre[::-1] and suf in seen and seen[suf] != i:
                    ans.append([seen[suf], i])
                if j != len(w) and suf == suf[::-1] and pre in seen and seen[pre] != i:
                    ans.append([i , seen[pre]])
        return ans