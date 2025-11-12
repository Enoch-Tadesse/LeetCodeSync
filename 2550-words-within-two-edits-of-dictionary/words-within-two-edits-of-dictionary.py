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
            return used <= 2 and node.is_end
        if used == 2:
            idx = ord(word[i]) - ord('a')
            return self.search(node.chs[idx], word, i + 1, used)
        ans = False
        idx = ord(word[i]) - ord('a')
        for j, chs in enumerate(node.chs):
            if not chs:
                continue
            ans |= self.search(chs, word, i + 1, used + int(idx != j))
        return bool(ans)
 

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        ans = []
        for q in queries:
            if trie.search(trie, q, 0, 0):
                ans.append(q)
        return ans