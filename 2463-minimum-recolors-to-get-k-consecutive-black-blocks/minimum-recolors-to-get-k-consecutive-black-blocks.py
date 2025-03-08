class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float("inf")
        l = 0
        curr = 0
        for r in range(len(blocks)):
            if r - l + 1 < k:
                curr += int(blocks[r] == "W")
                continue
            curr += int(blocks[r] == "W")
            res = min(res, curr)
            curr -= int(blocks[l] == "W")
            l += 1
        return res