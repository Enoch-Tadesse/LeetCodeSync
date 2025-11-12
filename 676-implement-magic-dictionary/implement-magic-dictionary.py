class Trie:
    def __init__(self):
        self.chs = [None] * 26
        self.is_end = False

    def insert(self, word):
        curr = self
        for i , w in enumerate(word):
            idx = ord(w) - ord('a')
            if not curr.chs[idx]:
                curr.chs[idx] = Trie()
            curr = curr.chs[idx]
        curr.is_end = True

    def search(self, node, word,i , used):
        if not node:
            return False
        if i == len(word):
            return used and node.is_end
        if used:
            idx = ord(word[i]) - ord('a')
            return self.search(node.chs[idx], word, i + 1, used)
        ans = False
        idx = ord(word[i]) - ord('a')
        for j, chs in enumerate(node.chs):
            if not chs:
                continue
            ans |= self.search(chs, word, i + 1, idx != j)
        return bool(ans)
        # curr = self
        # for i , w in enumerate(word):
        #     idx = ord(w) - ord('a')
        #     if not curr.chs[idx]:
        #         return False
        #     curr = curr.chs[idx]
        # return curr.is_end

class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(self.trie, searchWord, 0, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)