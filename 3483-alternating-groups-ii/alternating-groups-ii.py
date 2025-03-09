class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        curr = 0
        counter = 0
        l = 0
        n = len(colors)
        for r in range(1, len(colors) + k - 1):
            if r - l + 1 < k:
                curr += int(colors[r] != colors[r-1])
                continue
            r %= n
            l %= n
            if colors[r] != colors[r-1]:
                curr += 1
            counter += int(curr == k - 1)
            if colors[l] != colors[(l+1) % n]:
                curr -= 1
            l += 1
        return counter            