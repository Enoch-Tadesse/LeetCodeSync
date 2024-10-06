class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        size = len(stones)
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while size > 1:
            a = -1*heapq.heappop(stones)
            b = -1*heapq.heappop(stones)
            # print(stones)
            if a != b:
                heapq.heappush(stones,-1*abs(a-b))
                size-=1
            else:
                size-=2
        return 0 if not size else -1 * stones[0]