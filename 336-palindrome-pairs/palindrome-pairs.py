class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        rev = {word : i for i, word in enumerate(words)}

        ans = set()

        for curr, word in enumerate(words):
            n = len(word)

            for i in range(n + 1):
                left = word[:i]
                right = word[i:] if i < n else ""


                if left == left[::-1] and right[::-1] in rev:
                    new_idx = rev[right[::-1]]
                    if new_idx != curr:
                        ans.add((new_idx,curr))

                if right == right[::-1] and left[::-1] in rev:
                    new_idx = rev[left[::-1]]
                    if curr != new_idx:
                        ans.add((curr, new_idx))          

        return list(ans)

            