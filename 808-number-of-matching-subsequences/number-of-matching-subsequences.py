class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def idx(c):
            return ord(c) - ord('a')
        ans = 0
        counts = [[] for _ in range(26)]
        for i in range(len(s)):
            counts[idx(s[i])].append(i)
        for w in words:
            curr = -1
            for c in w:
                arr = counts[idx(c)]
                if not arr:
                    break
                pos = bisect_right(arr, curr)
                if pos == len(arr):
                    break
                curr = arr[pos]
                # while state[index] < len(counts[index]) and counts[index][state[index]] <= curr:
                #     state[index] += 1
                # if state[index] == len(counts[index]):
                #     break
                # curr = counts[index][state[index]]            
            else:
                ans += 1
        return ans