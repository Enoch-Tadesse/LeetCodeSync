class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = [0,nums[0]]
        for i in range(1, len(nums)):
            self.preSum.append(nums[i] + self.preSum[i])
        print(self.preSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)