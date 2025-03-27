class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        curr = nums[0]
        curr_count = 1
        for i in range(1, len(nums)):
            if curr == nums[i]:
                curr_count += 1
            else:
                curr_count -= 1
            if curr_count == 0:
                curr = nums[i]
                curr_count = 1
            # print(curr, curr_count)
        dom = nums.count(curr)
        # print(curr, dom)
        left = 0
        for i in range(len(nums)):
            if nums[i] == curr:
                left += 1
            left_dom = (i + 1) / 2 < left
            right_dom = (len(nums) - i - 1) / 2 < (dom - left)
            if left_dom and right_dom:
                return i
        return -1