class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        size = len(stones)
        heapq._heapify_max(stones)
        while size > 1:
            # print(stones)
            a = heapq._heappop_max(stones)
            # a = stones.pop()
            b = heapq._heappop_max(stones)
            # b = stones.pop()
            print(stones)
            if a - b != 0:
                # heapq.heappush(stones,abs(a-b))
                stones.append(abs(a-b))
                heapq._heapify_max(stones)
                size-=1
            else:
                size-=2
        if size == 0:
            return 0
        else:
            return stones[0]