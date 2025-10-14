class Trie:
    def __init__(self):
        self.children = {}
        self.sum = 0

    def insert(self, word, val):
        root = self
        for w in word:
            if w not in root.children:
                root.children[w] = Trie()
            root = root.children[w]
            root.sum += val
    
    def query(self, word):
        root = self
        for w in word:
            if w not in root.children:
                return 0
            root = root.children[w]
        return root.sum

class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        if key not in self.map:
            self.trie.insert(key, val)
            self.map[key] = val
        else:
            diff = val - self.map[key]
            self.trie.insert(key, diff)
            self.map[key] = val


    def sum(self, prefix: str) -> int:
        return self.trie.query(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)