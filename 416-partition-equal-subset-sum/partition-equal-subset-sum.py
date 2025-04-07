class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2
        seen = set()
        seen.add(0)
        for i in range(len(nums)):
            temp = list(seen)
            for num in temp:
                if num + nums[i] == target:
                    return True
                seen.add(num + nums[i])
        return False

