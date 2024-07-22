class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            nums = 0
            power = len(digits) - 1
            for i in range(len(digits)):
                nums+=int(digits[i]) * (10**power)
                power-=1
            nums += 1
            nums = list(str(nums))
            return [int(num) for num in nums]