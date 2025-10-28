class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # if they are equal, moving right and left are possible
        # if the right or left dominates just by one, only one is possible
        counter = 0
        pre = []
        curr = 0
        for num in nums:
            curr += num
            pre.append(curr)
        suf = [0] * len(nums)
        curr = 0
        for i in range(len(nums)-1, -1, -1):
            curr += nums[i]
            suf[i] = curr
        # print(pre)
        # print(suf)
        for i in range(len(nums)):
            if nums[i] == 0:
                if pre[i] == suf[i]:
                    counter += 2
                elif abs(pre[i] - suf[i]) == 1:
                    counter += 1
        return counter