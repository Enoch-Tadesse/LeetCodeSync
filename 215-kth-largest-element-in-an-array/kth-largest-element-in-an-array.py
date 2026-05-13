class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num)
            else:
                top = min_heap[0]
                if top < num:
                    heappop(min_heap)
                    heappush(min_heap, num)
        return min_heap[0]