class Trie:
    def __init__(self):
        self.chs = [None for _ in range(26)]
        self.is_end = False
    @lru_cache
    def can_seg(self, master, i, root):
        if i == len(master):
            return True # adjust
        for j in range(i , len(master)):
            idx = ord(master[j]) - ord('a')
            if not root.chs[idx]:
                return False
            root = root.chs[idx]
            if not root.is_end:
                continue
            if self.can_seg(master, j + 1, self):
                return True
        return root.is_end

    def insert(self, word):
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                root.chs[idx] = Trie()
            root = root.chs[idx]
        root.is_end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # record the words,
        # use recursion for segmenting,
        # if found, 2 ops, (take it, proceed normally)
        # look for bools
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        return trie.can_seg(s, 0, trie)