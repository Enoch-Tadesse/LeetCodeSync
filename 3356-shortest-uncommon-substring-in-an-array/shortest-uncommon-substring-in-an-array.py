class Trie:
    def __init__(self):
        self.chs = [None for _ in range(26)]
        self.is_end = False
        self.count = set()
    def insert(self, word, label):
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                root.chs[idx] = Trie()
            root = root.chs[idx]
        root.count.add(label)
        root.is_end = True
    def check(self, word):
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                return True
            root = root.chs[idx]
        return len(root.count) <= 1

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        trie = Trie()
        words = arr
        for idx, word in enumerate(words):
            for i in range(len(word)):
                for j in range(i + 1, len(word)+1):
                    check = word[i:j]
                    trie.insert(check, idx)
        ans = [""] * len(words)
        for idx, word in enumerate(words):
            for i in range(len(word)):
                for j in range(i + 1, len(word)+1):
                    check = word[i:j]

                    if not trie.check(check):
                        continue
                    if ans[idx]:
                        if len(ans[idx]) > len(check):
                            ans[idx] = check
                        elif len(ans[idx]) == len(check):
                            ans[idx] = min(ans[idx], check)
                    else:
                        ans[idx] = check
                    break
        return ans