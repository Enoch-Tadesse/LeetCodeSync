class Trie:
    def __init__(self):
        self.chs = [None for _ in range(26)]
        self.index = float("inf")
        self.length = float("inf")

    def insert(self, word, i):
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                root.chs[idx] = Trie()
            root = root.chs[idx]
            if root.length > len(word):
                root.index = i
                root.length = len(word)

    def solve(self, word):
        root = self
        ans = float("inf")
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                return ans
            root = root.chs[idx]
            ans = root.index
        return ans
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        fall = ["", float("inf"), -1] # string, len, idx
        trie = Trie()
        for i , word in enumerate(wordsContainer):
            trie.insert(word[::-1], i)
            if len(word) < fall[1]:
                fall[0], fall[1], fall[2] = word, len(word), i
        fallidx = fall[2]
        ans = []
        for query in wordsQuery:
            cand = trie.solve(query[::-1])
            if cand == float("inf"):
                ans.append(fallidx)
            else:
                ans.append(cand)
        return ans
        """
        finding is simple, if not found, what to return is the smallest length that occurred first.
        """