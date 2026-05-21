class Trie:
    def __init__(self):
        self.children = [None for _ in range(10)]
    def insert(self, num):
        num = str(num)
        curr = self
        for n in num:
            i = int(n)
            if not curr.children[i]:
                curr.children[i] = Trie()
            curr = curr.children[i]
    
    def find(self, num):
        num = str(num)
        curr = self
        i = 0
        while i < len(num):
            n = int(num[i])
            if not curr.children[n]:
                return i
            curr = curr.children[n]
            i += 1
        return i


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(num)
        ans = 0
        for num in arr2:
            ans = max(ans, trie.find(num))
        return ans