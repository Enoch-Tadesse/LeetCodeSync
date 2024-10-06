class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        size = len(stones)
        heapq._heapify_max(stones)
        while size > 1:
            a = heapq._heappop_max(stones)
            b = heapq._heappop_max(stones)
            # print(stones)
            if a - b != 0:
                stones.append(abs(a-b))
                heapq._heapify_max(stones)
                size-=1
            else:
                size-=2
        return 0 if not size else stones[0]