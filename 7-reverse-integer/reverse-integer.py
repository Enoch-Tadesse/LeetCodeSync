class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31 or x < -2**31:
            return 0
        else:
            nums = []
            y=0
            isNegative = False
            if x < 0:
                x*=-1
                isNegative = True
            while x > 0:
                nums.append(x%10)
                x = x // 10
            digit = len(nums)
            for num in nums:
                y+=((10**(digit-1))*num)
                digit-=1
            if y > 2**31 or y < -2**31:
                return 0
            if isNegative:
                return y*-1
            return y
