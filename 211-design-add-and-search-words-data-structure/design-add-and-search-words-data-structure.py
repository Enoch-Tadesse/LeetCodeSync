class Trie:
    def __init__(self):
        self.chs = [None for _ in range(26)]
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        root = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                root.chs[idx] = Trie()
            root = root.chs[idx]
        root.end = True

    def srh(self, word, i,  root):
        if i == len(word):
            return root.end
        for j in range(i , len(word)):
            w = word[j]
            if w == ".":
                for r in root.chs:
                    if not r:
                        continue
                    if self.srh(word, j + 1, r):
                        return True
                return False
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                return False
            root = root.chs[idx]
        return root.end

    def search(self, word: str) -> bool:
        return self.srh(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)