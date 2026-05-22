class Trie:
    def __init__(self):
        self.ch = [None for _ in range(26)]
        self.end = False
        self.cnt = 0
    def insert(self, word):
        curr = self
        for w in word:
            curr.cnt += 1
            idx = ord(w) - ord('a')
            if not curr.ch[idx]:
                curr.ch[idx] = Trie()
            curr = curr.ch[idx]
        curr.end = True

    def find(self):
        ans = []
        temp = []
        def dfs(curr):
            if curr.end and not curr.cnt:
                val = "".join(temp)
                ans.append(val[::-1])
                return
            for i, nei in enumerate(curr.ch):
                if nei:
                    temp.append(chr(i + ord('a')))
                    dfs(nei)
                    temp.pop()
        dfs(self)
        return ans

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word[::-1])
        ans = trie.find()
        total = len(ans)
        for a in ans:
            total += len(a)
        return total