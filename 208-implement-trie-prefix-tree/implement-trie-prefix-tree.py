class Trie:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

    def insert(self, word: str) -> None:
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if root.children[idx] == None:
                root.children[idx] = Trie()
            root = root.children[idx]
        root.is_end = True

    def search(self, word: str) -> bool:
        root = self
        for i , w in enumerate(word):
            idx = ord(w) - ord('a')
            if root.children[idx] == None:
                return False
            root = root.children[idx]
        return root.is_end

    def startsWith(self, prefix: str) -> bool:
        root = self
        for i , w in enumerate(prefix):
            idx = ord(w) - ord('a')
            if root.children[idx] == None:
                return False
            root = root.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)