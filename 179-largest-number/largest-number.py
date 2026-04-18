class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        [3,30,34,5,9]
        
        [9, 5,  34,  3, 30]

        nums = [str(num) for num in nums]

        def compare(num1, num2):
            pos1, pos2 = num1 + num2, num2 + num1
            if int(pos1) > int(pos2):
                return True
            return False
        

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i):
                if not compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        ans = "".join(nums)
        return str(int(ans))
        