class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        seen = {w[::-1] : i for i , w in enumerate(words)}
        ans = set()
        for i , w in enumerate(words):
            for j in range(len(w) + 1):
                pre , suf = w[:j] , w[j:]
                if pre == pre[::-1] and suf in seen and seen[suf] != i:
                    ans.add((seen[suf], i))
                if suf == suf[::-1] and pre in seen and seen[pre] != i:
                    ans.add((i , seen[pre]))
        return [[l , r] for l , r in ans]