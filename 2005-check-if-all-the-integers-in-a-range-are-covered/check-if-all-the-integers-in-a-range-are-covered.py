class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover = set([i for i in range(left,right + 1)])
        for l , r in ranges:
            for i in range(l,r+1):
                if i in cover:
                    cover.remove(i)
        if len(cover)!=0:
            return False
        return True
