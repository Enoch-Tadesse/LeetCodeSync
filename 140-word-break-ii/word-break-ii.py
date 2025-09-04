class Trie:
    def __init__(self):
        self.chs = [None for _ in range(26)]
        self.is_end = False

    def can_seg(self, word, i, cont , temp, root):
        if i == len(word):
            cont.append(" ".join(temp))
            return True
        for j in range(i , len(word)):
            idx = ord(word[j]) - ord('a')
            if not root.chs[idx]:
                return False
            root = root.chs[idx]
            if not root.is_end:
                continue
            temp.append(word[i:j+1])
            self.can_seg(word, j + 1, cont, temp, self)
            temp.pop()
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
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        cont = []
        trie.can_seg(s, 0 , cont, [], trie)
        return cont