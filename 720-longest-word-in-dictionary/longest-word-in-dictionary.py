class Trie:
    def __init__(self):
        self.end = False
        self.children = {}

    def insert(self, word):
        root = self
        for w in word:
            if w not in root.children:
                root.children[w] = Trie()
            root = root.children[w]
        root.end = True
    
    def query(self, word):
        root = self
        for w in word:
            root = root.children[w]
            if not root.end:
                return False
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda x : (-len(x), x))
        trie = Trie()
        for w in words:
            trie.insert(w)
        for w in words:
            if trie.query(w):
                return w
        return ""