class Trie:
    def __init__ (self):
        self.chs = [None for _ in range(26)]
        self.count = 0
    def insert(self, word):
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                root.chs[idx] = Trie()
            root = root.chs[idx]
            root.count += 1
    def get_common(self, size):
        root = self
        ans = []
        carry = True
        while carry:
            for i in range(26):
                r = root.chs[i]
                if not r:
                    continue
                if r.count == size:
                    ans.append(chr(ord('a') + i))
                    root = root.chs[i]
                    break
            else:
                carry = False
        return "".join(ans)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)
        return trie.get_common(len(strs))
