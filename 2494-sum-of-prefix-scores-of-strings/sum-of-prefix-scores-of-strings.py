class Trie:
    def __init__(self):
        self.count = 0
        self.children = dict()

    def insert(self, word):
        root = self
        for w in word:
            if w not in root.children:
                root.children[w] = Trie()
            root = root.children[w]
            root.count += 1

    def query(self, word):
        root = self
        ans = 0
        for w in word:
            root = root.children[w]
            ans += root.count
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.query(word))
        return ans