class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reverse = {word[::-1] : i for i, word in enumerate(words)}

        ans = set()

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                pre , suf = word[:j], word[j:]

                if pre == pre[::-1] and suf in reverse and reverse[suf] != i:
                    ans.add((reverse[suf], i))

                if suf == suf[::-1] and pre in reverse and reverse[pre] != i:
                    ans.add((i, reverse[pre]))


        return list(ans)