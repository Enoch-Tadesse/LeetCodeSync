class Trie:
    def __init__(self):
        self.chs = [None for _ in range(26)]
        self.is_end = False

    def insert(self, word):
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                root.chs[idx] = Trie()
            root = root.chs[idx]
        root.is_end = True
            
    def search(self, word):
        root = self
        for w in reversed(word):
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                return False
            root = root.chs[idx]
            if root.is_end:
                return True
        return root.is_end
class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        return self.trie.search(self.stream)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)