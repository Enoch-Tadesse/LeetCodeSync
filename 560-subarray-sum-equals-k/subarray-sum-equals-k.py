class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        preSum = 0
        fre = defaultdict(int)
        fre[0] = 1
        for num in nums:
            preSum += num
            if (preSum-k) in fre:
                count+=fre[preSum-k]
            fre[preSum]+=1
        return count

        # 0,1,2,3