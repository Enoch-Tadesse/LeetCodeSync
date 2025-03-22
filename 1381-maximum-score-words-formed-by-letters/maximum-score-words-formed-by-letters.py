class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters = Counter(letters)
        helper = defaultdict(lambda : [Counter(), 0]) # counts, score
        offset = ord('a')
        for word in words:
            helper[word][0] = Counter(word)
            helper[word][1] = sum(score[ord(i) - offset] for i in word)
        self.ans = 0
        self.temp = []
        self.back(words, 0, letters, 0, helper)
        return self.ans

    def back(self, words, start, counts, curr, helper):
        if start == len(words):
            self.ans = max(self.ans , curr)
            return
        for i in range(start, len(words)):
            for let , freq in helper[words[i]][0].items():
                if freq > counts[let]:
                    break
            else:
                for let , freq in helper[words[i]][0].items():
                    counts[let] -= freq
                self.temp.append(words[i])
                self.back(words, i + 1, counts, curr + helper[words[i]][1], helper)
                self.temp.pop()
                for let , freq in helper[words[i]][0].items():
                    counts[let] += freq
        self.ans = max(self.ans, curr) # this line was a pain in the ass
                