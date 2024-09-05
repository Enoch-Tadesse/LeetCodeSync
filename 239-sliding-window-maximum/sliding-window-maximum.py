class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deq = deque()
        i = 0
        j = 0
        while j < len(nums):
            while deq and nums[deq[-1]] < nums[j]:
                deq.pop()
            deq.append(j)
            if i > deq[0]:
                deq.popleft()
            if j + 1 >= k:
                res.append(nums[deq[0]])
                i+=1
            
            j+=1
        return res