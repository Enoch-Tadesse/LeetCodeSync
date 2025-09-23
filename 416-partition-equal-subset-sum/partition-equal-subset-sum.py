class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2
        nums.sort()
        curr = set([0])
        for num in nums:
            new = list(curr)
            for ele in new:
                curr.add(num + ele)
            if target in curr:
                return True
        return False