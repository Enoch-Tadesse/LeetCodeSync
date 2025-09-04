class Trie:
    def __init__(self):
        self.chs = [None for _ in range(26)]
        self.is_end = False
        self.words = []

    def candidate(self, word):
        if word in self.words:
            return
        self.words.append(word)
        self.words.sort()
        if (len(self.words) > 3) :
            self.words.pop()
        

    def suggest(self, word):
        ans = []
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                root.chs[idx] = Trie()
            root = root.chs[idx]
            ans.append(root.words)
        return ans

    def insert(self, word):
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                root.chs[idx] = Trie()
            root = root.chs[idx]
            root.candidate(word)
        root.is_end = True
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for pro in products:
            trie.insert(pro)
        return trie.suggest(searchWord)