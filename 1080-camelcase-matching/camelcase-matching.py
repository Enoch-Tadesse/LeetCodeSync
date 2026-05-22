class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        for word in queries:
            i , j = 0 , 0
            while i < len(word) and j < len(pattern):
                if word[i] == pattern[j]:
                    i += 1
                    j += 1
                elif word[i].isupper():
                    ans.append(False)
                    break
                else: i += 1
            else:
                if j != len(pattern):
                    ans.append(False)
                else:
                    stat = True
                    while i < len(word):
                        if word[i].isupper():
                            stat = False
                            break
                        i += 1
                    ans.append(stat)
        return ans