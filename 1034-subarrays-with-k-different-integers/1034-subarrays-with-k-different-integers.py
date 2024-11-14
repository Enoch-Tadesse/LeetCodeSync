class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res = 0
        l_near = 0
        l_far = 0
        count = defaultdict(int)

        for r in range(len(nums)):
            count[nums[r]] += 1
            while len(count) > k:
                count[nums[l_near]] -= 1
                if count[nums[l_near]] == 0:
                    count.pop(nums[l_near])
                l_near += 1
                l_far = l_near
            while count[nums[l_near]] > 1:
                count[nums[l_near]] -= 1
                l_near+=1
            if len(count) == k:
                res += l_near - l_far + 1
        return res
        
        
        # res = 0
        # counter = defaultdict(int)

        # n = len(nums)

        # l = 0
        # r = 0
        # while r < n:
        #     if r - l + 1 < k:
        #         counter[nums[r]] += 1
        #         r+=1
        #         continue
        #     counter[nums[r]] += 1
        #     if len(counter) < k:
        #         r+=1
        #         continue
        #     elif len(counter) == k:
        #         res += 1
        #         for s in range(r+1,n):
        #             if nums[s] in counter:
        #                 res+=1
        #                 continue
        #             break
        #     counter[nums[l]] -= 1
        #     if counter[nums[l]] == 0:
        #         del counter[nums[l]]
        #     if r - l + 1 > k:
        #         counter[nums[r]]-=1
        #     else:
        #         r+=1
        #     l+=1


        # return res