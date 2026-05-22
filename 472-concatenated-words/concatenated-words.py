class Trie:
    def __init__(self):
        self.ch = [None for _ in range(26)]
        self.isend = False
        self.len = 0
    def insert(self, word):
        curr = self
        for w in word:
            idx = ord(w) - ord('a')
            if not curr.ch[idx]:
                curr.ch[idx] = Trie()
            curr = curr.ch[idx]
        curr.isend = True
        curr.len = len(word)

    def find(self, word):
        memo = {}
        
        def dfs(i, curr):
            if i in memo:
                return memo[i]

            if i == len(word):
                return curr.len != len(word) and curr.isend

            curr = self

            for j in range(i, len(word)):
                idx = ord(word[j]) - ord('a')
                if not curr.ch[idx]:
                    break
                    
                curr = curr.ch[idx]
                if curr.isend:
                    if dfs(j + 1, curr):
                        memo[i] = True
                        return True

            memo[i]= False
            return False
        return dfs(0, self)

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # it is easy but we must avoid accidentally picking the word itself
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            if trie.find(word):
                ans.append(word)
        return ans