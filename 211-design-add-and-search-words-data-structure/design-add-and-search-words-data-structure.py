class Trie:
    def __init__(self):
        self.children = dict()
        self.end = False

    def insert(self, word):
        root = self
        for w in word:
            if w not in root.children:
                root.children[w] = Trie()
            root = root.children[w]
        root.end = True

    def search(self, word):
        stack = [(self, 0)] # stores (node, idx)
        while stack:
            node, idx = stack.pop()
            if idx == len(word):
                if node.end:
                    return True
                continue
            char = word[idx]
            if char != ".":
                if char in node.children:
                    stack.append((node.children[char], idx + 1))
            else:
                for child in node.children:
                    stack.append((node.children[child], idx + 1))
        return False
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)